import os
import pytest
from unittest.mock import patch
from typing import Optional
from core.openai_client import OpenAIClient
from openai.error import OpenAIError

@pytest.fixture
def mock_api_key():
    with patch.dict(os.environ, {"OPENAI_API_KEY": "your_test_api_key"}, clear=True):
        yield

def test_openai_client_init(mock_api_key):
    client = OpenAIClient()
    assert client.api_key == "your_test_api_key"

@patch('openai.Completion.acreate')
def test_generate_text_basic(mock_acreate, mock_api_key):
    mock_acreate.return_value = {"choices": [{"text": "Hello, world!"}]} 
    client = OpenAIClient()
    response = client.generate_text(prompt="Say hello.")
    assert response == "Hello, world!"
    mock_acreate.assert_called_once_with(engine='text-davinci-003', prompt='Say hello.', temperature=0.7, max_tokens=None, top_p=None, frequency_penalty=None, presence_penalty=None)

@patch('openai.Completion.acreate')
def test_generate_text_with_parameters(mock_acreate, mock_api_key):
    mock_acreate.return_value = {"choices": [{"text": "This is a test"}]}
    client = OpenAIClient()
    response = client.generate_text(prompt="Write a short sentence.", temperature=0.5, max_tokens=10)
    assert response == "This is a test"
    mock_acreate.assert_called_once_with(engine='text-davinci-003', prompt='Write a short sentence.', temperature=0.5, max_tokens=10, top_p=None, frequency_penalty=None, presence_penalty=None)

@patch('openai.Completion.acreate', side_effect=OpenAIError('Error during API call', '400', None))
def test_generate_text_error(mock_acreate, mock_api_key):
    client = OpenAIClient()
    with pytest.raises(Exception) as e:
        client.generate_text(prompt="Test")
    assert str(e.value) == "OpenAI API Error: Error during API call"

@patch('openai.Completion.acreate', return_value={"choices": []})
def test_generate_text_no_choices(mock_acreate, mock_api_key):
    client = OpenAIClient()
    with pytest.raises(Exception) as e:
        client.generate_text(prompt="Test")
    assert str(e.value) == "OpenAI API Error: No response choices returned."