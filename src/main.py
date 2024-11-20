from streamlit import (
    title as st_title,
    container as st_container,
    empty as st_empty,
    expander as st_expander,
    slider as st_slider,
    button as st_button
)
from graph.app import GraphApp
from schemas.graph_state import GraphState
from utils.log import setup_log
from utils.settings import Settings

settings = Settings()

setup_log(settings)

graph_app = GraphApp(settings)

graph_state = GraphState()

st_title(settings.ST_TITLE)

with st_expander('Settings'):
    creativity = st_slider(
        'Creatitivy',
        value=1.,
        min_value=0.,
        max_value=1.,
        step=.1
    )

with st_container():
    option_a = st_empty()
    or_label = st_empty()
    option_b = st_empty()

    btn_generate = st_button(settings.ST_GENERATE_BUTTON)

    if btn_generate:
        graph_state.creativity = creativity
        graph_return = graph_app(graph_state)

        dilema_created = graph_return['dilema']
        option_a.markdown(f'### {dilema_created.option_a}')
        or_label.markdown('#### or...')
        option_b.markdown(f'### {dilema_created.option_b}')
