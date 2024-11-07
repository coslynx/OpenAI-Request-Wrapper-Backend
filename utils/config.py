import os
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    OPENAI_API_KEY: str = Field(..., env="OPENAI_API_KEY", description="Your OpenAI API key")
    DATABASE_URL: str = Field(..., env="DATABASE_URL", description="Connection string for your database")

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'