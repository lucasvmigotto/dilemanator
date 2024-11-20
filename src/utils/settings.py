from pathlib import Path
from typing import  Self

from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='../.env',
        env_ignore_empty=True,
        extra='ignore',
        env_prefix='APP__',
        case_sensitive=False
    )

    SEED: int = 42

    HOST: str = '0.0.0.0'
    PORT: int = 8080

    MODE_VERBOSE: bool = False
    MODE_DEBUG: bool = False

    LOG_LEVEL: str = 'DEBUG'
    LOG_DATE_FORMAT: str = '%Y-%m-%d %H:%M:%S'
    LOG_FORMAT: str = '%(asctime)s %(levelname:<8)s %(name)s: %(message)s'

    DILEMAS_SAMPLES_URL: str

    MODEL_NAME: str = 'gemini-1.5-flash'
    MODEL_TEMPERATURE: float = 1.
    MODEL_APIKEY: str

    PROMPTS_FOLDER: str = '/code/prompts'
    @computed_field
    @property
    def prompts_folder(self: Self) -> Path:
        return Path(self.PROMPTS_FOLDER)

    ST_TITLE: str = 'Dilemanator'
    ST_GENERATE_BUTTON: str = 'Generate'
    TOOLBARMODE: str = 'viewer'

