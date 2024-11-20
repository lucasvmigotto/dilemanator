from typing import Annotated
from pydantic import BaseModel, Field
from langgraph.graph import add_messages
from .dilema import Dilema


class GraphState(BaseModel):
    creativity: float = Field(
        description=(
            'Temperature to use in LLM'
        ),
        default=1.
    )
    topic: str = Field(
        description=(
            'Topic to direct LLM dilema'
            ' generation'
        ),
        default=None
    )
    dilema: Dilema = Field(
        description=(
            'Dilema created by the LLM'
        ),
        default=None
    )
    history: Annotated[list[Dilema], add_messages] = Field(
        description=(
            'History of dilemas generated'
            ' by the LLM model'
        ),
        default=[]
    )
