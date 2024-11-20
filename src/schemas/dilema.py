from pydantic import BaseModel, Field
from .enums.feedback import Feedback


class Dilema(BaseModel):
    option_a: str = Field(
        description=(
            'First option of the dilema'
        )
    )
    option_b: str = Field(
        description=(
            'First option of the dilema'
        )
    )
    feedback: int = Field(
        description=(
            'Feedback provided by the user'
            ' about the quality of the dilema'
        ),
        default=Feedback.NEUTRAL
    )
