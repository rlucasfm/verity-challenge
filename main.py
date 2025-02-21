from inference.simple_graph import SimpleGraphInferencer
from inference.agent_graph import AgentGraphInferencer


if __name__ == "__main__":
    inferencer = SimpleGraphInferencer()
    # inferencer = AgentGraphInferencer()
    print(inferencer.infer("Insira dois novos clientes chamados Caio Catto e Natan Natto"))