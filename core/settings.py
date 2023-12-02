from dotenv import load_dotenv
from pathlib import Path
from pydantic_settings import BaseSettings
import os


# Get .env

dotenv_path = Path(__file__).parent.parent / '.env'

load_dotenv(dotenv_path)

env = os.environ.get('ENV', 'dev')


if env == 'dev':
    class Settings(BaseSettings):
        app_name: str = "Project.env"
        version: str = "0.0.1dev"
        debug: bool = True
        testing: bool = True
        db_url: str = "postgresql://postgres:postgres@localhost:5432/Project.env"
        db_echo: bool = True
        enviroment: str = "dev"

elif env == 'staging':
    class Settings(BaseSettings):
        app_name: str = "Project.env"
        version: str = "1.0.0"
        debug: bool = False
        testing: bool = False
        db_url: str = ""
        db_echo: bool = False
        enviroment: str = "staging"

elif env == 'prod':
    class Settings(BaseSettings):
        app_name: str = "Project.env"
        version: str = "1.0.0"
        debug: bool = False
        testing: bool = False
        db_url: str = ""
        db_echo: bool = False
        enviroment: str = "prod"

else:
    raise ValueError('A variável de ambiente ENV deve ser dev, staging ou prod')
    

def get_settings():
    return Settings()