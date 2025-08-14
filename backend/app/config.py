"""
Legacy configuration module for backward compatibility.
Imports from core.config to maintain existing import paths.

Location: backend/app/config.py
"""

# Import all configuration from the core module
from app.core.config import *

# This module exists for backward compatibility
# All configuration should be imported from app.core.config going forward