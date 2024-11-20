from typing import Self
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from schemas.dilema import Dilema
from utils.settings import Settings
from utils.prompt import read_prompt_template, build_examples
from schemas.graph_state import GraphState


class DilemaGenerator:

    def __init__(
        self: Self,
        settings: Settings
    ):
        self.__model_name: str = settings.MODEL_NAME
        self.__model_temperature: str = settings.MODEL_TEMPERATURE
        self.__model_apikey: str = settings.MODEL_APIKEY
        self.prompt = ChatPromptTemplate(
            [
                (
                    'system',
                    read_prompt_template(
                        'base',
                        settings.prompts_folder
                    )
                ),
                ('placeholder', '{user_request}')
            ],
            partial_variables={
                'dilemas_examples': build_examples(
                    settings.DILEMAS_SAMPLES_URL
                )
            }
        )


    def __call__(
        self: Self,
        state: GraphState
    ):
        query: str = 'Please, give me a new dilema'
        if state.topic:
            query += f' about {state.topic}'

        input_content = {
            'user_request': [HumanMessage(query)]
        }

        chain = (
            self.prompt
            | ChatGoogleGenerativeAI(
                model=self.__model_name,
                temperature=(
                    state.creativity
                    if state.creativity
                    else self.__model_temperature
                ),
                api_key=self.__model_apikey
            ).with_structured_output(Dilema)
        )

        dilema_created: Dilema = chain.invoke(input_content)

        return {'dilema': dilema_created}
