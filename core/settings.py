from dotenv import load_dotenv
from pathlib import Path
from pydantic_settings import BaseSettings
import os, sys


# Get .env

dotenv_path = Path(__file__).parent.parent / '.env'

load_dotenv(dotenv_path)

env = sys.argv[1]


if env == 'dev':
    class Settings(BaseSettings):
        app_name: str = "Project.env"
        version: str = "0.0.1dev"
        debug: bool = True
        testing: bool = True
        db_url: str = os.environ.get('SQLALCHEMY_DATABASE_URI_DEV')
        db_echo: bool = True
        enviroment: str = "dev"

elif env == 'hml':
    class Settings(BaseSettings):
        app_name: str = "Project.env"
        version: str = "1.0.0"
        debug: bool = False
        testing: bool = False
        db_url: str = os.environ.get('SQLALCHEMY_DATABASE_URI_HML')
        db_echo: bool = False
        enviroment: str = "hml"

elif env == 'prd':
    class Settings(BaseSettings):
        app_name: str = "Project.env"
        version: str = "1.0.0"
        debug: bool = False
        testing: bool = False
        db_url: str = os.environ.get('SQLALCHEMY_DATABASE_URI_PRD')
        db_echo: bool = False
        enviroment: str = "prd"

else:
    raise ValueError('A variável de ambiente ENV deve ser dev, hml ou prd')
    

def get_settings():
    return Settings()