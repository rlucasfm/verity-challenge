from langchain_community.utilities import SQLDatabase
from langchain.chat_models import init_chat_model
from langchain import hub
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langgraph.prebuilt import create_react_agent

class AgentGraphInferencer:
    def __init__(self):
        self.llm = init_chat_model("gpt-4o-mini", model_provider="openai")
        self.prompt_template = hub.pull("langchain-ai/sql-agent-system-prompt")
        self.db = SQLDatabase.from_uri("sqlite:///database.db")
        
        toolkit = SQLDatabaseToolkit(db=self.db, llm=self.llm)
        self.tools = toolkit.get_tools()
        self.system_message = self.prompt_template.format(dialect="SQLite", top_k=5)
        
    def infer(self, query: str):
        agent_executor = create_react_agent(self.llm, self.tools, prompt=self.system_message)

        for step in agent_executor.stream(
            {"messages": [
                {"role": "system", "content": "You can't alter the database, create tables, insert, update or delete data, only query the database for viewing data. Your last answer must be in portuguese."}, 
                {"role": "user", "content": query}
            ]},
        ):
            if 'agent' in step:
                if step['agent']['messages'][0].response_metadata['finish_reason'] == 'stop':
                    return step['agent']['messages'][0].content