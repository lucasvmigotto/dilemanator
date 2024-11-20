from typing import Self
from langgraph.graph import START, END, StateGraph

from graph.nodes.dilema_generator import DilemaGenerator
from utils.settings import Settings
from schemas.graph_state import GraphState


class GraphApp:

    def __init__(
        self: Self,
        settings: Settings
    ):
        workflow = StateGraph(GraphState)
        workflow.add_node(
            'generate_dilema',
            DilemaGenerator(settings)
        )
        workflow.add_edge(START, 'generate_dilema')
        workflow.add_edge('generate_dilema', END)

        self.__app = workflow.compile()

    def __call__(
        self: Self,
        state: GraphState
    ):
        return self.__app.invoke(state)
