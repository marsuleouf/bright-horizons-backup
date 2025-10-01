"""Pytest configuration and shared fixtures."""

import asyncio
import os
from unittest.mock import patch

import pytest


@pytest.fixture(scope="session")
def event_loop():
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture
def mock_env():
    """Mock environment variables for testing."""
    with patch.dict(os.environ, {"BH_EMAIL": "test@example.com", "BH_PASSWORD": "test_password"}, clear=True):
        yield


@pytest.fixture
def clean_env():
    """Clean environment variables for testing."""
    with patch.dict(os.environ, {}, clear=True):
        yield
