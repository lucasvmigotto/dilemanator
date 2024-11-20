from pathlib import Path
from streamlit import cache_data as st_cache_data
from pandas import read_csv, DataFrame

@st_cache_data
def build_examples(samples_url: str) -> str:
    df_dilemas: DataFrame = read_csv(samples_url)

    template: str = '''

    Dilema #{index}
    - {option_a}
    or
    - {option_b}

    '''

    return '---'.join([
        template.format(
            index=index + 1,
            option_a=option_a,
            option_b=option_b
        )
        for index, (option_a, option_b) in df_dilemas.iterrows()
    ])


def read_prompt_template(
    prompt: str,
    prompts_folder: Path
) -> str:
    filename: Path = prompts_folder / (
        prompt
        if prompt.endswith('.md')
        else f'{prompt}.md'
    )
    content: str = None

    with open(filename) as file_ref:
        content = file_ref.read()

    return content
