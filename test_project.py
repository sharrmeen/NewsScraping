import pytest
import requests
from project import summarize_article,rps,shorten_url
from unittest.mock import patch


def test_summarize_article():
    url="https://news.google.com/articles/CBMimgFodHRwczovL3RpbWVzb2ZpbmRpYS5pbmRpYXRpbWVzLmNvbS92aWRlb3MvaXNyYWVsaS1qZXRzLXN0cmlrZS10YXJnZXQtc3lyaWFuLWFybXktb3V0cG9zdHMtaW4taG9tcy1wcm92aW5jZS10aHJlZS1jaXZpbGlhbnMta2lsbGVkL3ZpZGVvc2hvdy8xMDc0ODQ3OTkuY21z0gGeAWh0dHBzOi8vdGltZXNvZmluZGlhLmluZGlhdGltZXMuY29tL3ZpZGVvcy9pc3JhZWxpLWpldHMtc3RyaWtlLXRhcmdldC1zeXJpYW4tYXJteS1vdXRwb3N0cy1pbi1ob21zLXByb3ZpbmNlLXRocmVlLWNpdmlsaWFucy1raWxsZWQvYW1wX3ZpZGVvc2hvdy8xMDc0ODQ3OTkuY21z?hl=en-IN&gl=IN&ceid=IN%3Aen"
    summary=summarize_article(url)
    assert summary!=""
    url="https://invalid-url.com"
    summary = summarize_article(url)
    assert summary.startswith("Error:")

def test_rps():
    with patch('random.choice', return_value='scissors'):
        assert rps('rock') == "You win!"
    with patch('random.choice', return_value='paper'):
        assert rps('paper') == "It's a tie!"
    with patch('random.choice', return_value='rock'):
        assert rps('scissors') == "Computer wins!"

def test_shorten_url():
    # Mock the requests.get function to return a fixed response
    with patch('requests.get') as mock_get:
        # Set up the mock response
        mock_get.return_value.text = 'https://tinyurl.com/abcd123'

        # Call the function being tested
        shortened_url = shorten_url('https://www.example.com')

        # Assert that the function returns the expected shortened URL
        assert shortened_url == 'https://tinyurl.com/abcd123'

        # Assert that requests.get was called with the correct arguments
        mock_get.assert_called_once_with('https://tinyurl.com/api-create.php', params={'url': 'https://www.example.com'})
    # Mock the requests.get function to simulate an error response
    with patch('requests.get') as mock_get:
        # Set up the mock response to raise an exception
        mock_get.side_effect = requests.RequestException('Error fetching URL')
        shortened_url=shorten_url('https://www.example.com')
        assert shortened_url is None

        # Assert that requests.get was called with the correct arguments
        mock_get.assert_called_once_with('https://tinyurl.com/api-create.php', params={'url': 'https://www.example.com'})
     


