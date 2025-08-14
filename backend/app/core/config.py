# app/core/config.py
"""
Configuration settings for SmartBuy Backend
"""
from functools import lru_cache
from pathlib import Path
from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings with validation and environment variable support."""
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False
    )
    
    # Application settings
    app_name: str = "SmartBuy Deal Aggregation Engine"
    debug: bool = Field(default=True, description="Enable debug mode")
    host: str = Field(default="127.0.0.1", description="Host to bind the server")
    port: int = Field(default=8000, description="Port to bind the server")
    
    # Database settings
    database_url: str = Field(
        default="sqlite+aiosqlite:///./smartbuy.db",
        description="Database URL for SQLAlchemy"
    )
    database_echo: bool = Field(
        default=False,
        description="Enable SQLAlchemy query logging"
    )
    
    # API settings
    api_v1_prefix: str = "/api/v1"
    
    # Logging settings
    log_level: str = Field(default="INFO", description="Logging level")
    
    @property
    def database_path(self) -> Path:
        """Get the database file path for SQLite."""
        if "sqlite" in self.database_url:
            # Extract path from sqlite+aiosqlite:///./smartbuy.db
            path_part = self.database_url.split("///")[-1]
            return Path(path_part)
        return Path("smartbuy.db")


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()


