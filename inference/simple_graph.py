from langchain_community.tools.sql_database.tool import QuerySQLDatabaseTool
from langchain_community.utilities import SQLDatabase
from typing_extensions import TypedDict
from langchain.chat_models import init_chat_model
from langchain import hub
from typing_extensions import Annotated
from langgraph.graph import START, StateGraph

class State(TypedDict):
    question: str
    query: str
    result: str
    answer: str

class QueryOutput(TypedDict):
    """Generated SQL query."""

    query: Annotated[str, ..., "Syntactically valid SQL query."]


class SimpleGraphInferencer:
    def __init__(self):
        self.db = SQLDatabase.from_uri("sqlite:///database.db")
        self.llm = init_chat_model("gpt-4o-mini", model_provider="openai")
        self.query_prompt_template = hub.pull("langchain-ai/sql-query-system-prompt")

    def write_query(self, state: State):
        """Generate SQL query to fetch information."""
        prompt = self.query_prompt_template.invoke(
            {
                "dialect": self.db.dialect,
                "top_k": 10,
                "table_info": self.db.get_table_info(),
                "input": state["question"],
            }
        )
        structured_llm = self.llm.with_structured_output(QueryOutput)
        result = structured_llm.invoke(prompt)
        return {"query": result["query"]}

    def execute_query(self, state: State):
        """Execute SQL query."""
        if any(
            keyword in state["query"].lower()
            for keyword in ("update", "insert", "create", "drop", "alter")
        ):
            return {"result": "You are not allowed to modify the database."}
        execute_query_tool = QuerySQLDatabaseTool(db=self.db)
        return {"result": execute_query_tool.invoke(state["query"])}

    def generate_answer(self, state: State):
        """Answer question using retrieved information as context."""
        prompt = (
            "Dada a seguinte pergunta do usuário, a consulta SQL correspondente, "
            "e o resultado SQL, responda à pergunta do usuário.\n\n"
            f'Pergunta: {state["question"]}\n'
            f'Consulta SQL: {state["query"]}\n'
            f'Resultado SQL: {state["result"]}'
        )
        response = self.llm.invoke(prompt)
        return {"answer": response.content}

    def infer(self, query: str):
        graph_builder = StateGraph(State).add_sequence(
            [self.write_query, self.execute_query, self.generate_answer]
        )
        graph_builder.add_edge(START, "write_query")
        graph = graph_builder.compile()

        for step in graph.stream(
            {"question": query}
        ):
            if "generate_answer" in step:
                return step["generate_answer"]["answer"]