#!/usr/bin/env python3
"""Module for testing client"""


from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Class for Testing Github Org Client"""

    @parameterized.expand([
        ('google'),
        ('abc')
        ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """Test GithubOrgClient.org and see if it returns the correct value"""
        test_class = GithubOrgClient(input)
        test_class.org()
        mock.assert_called_once_with(
                f'https://api.github.com/orgs/{input}')

    
    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that the result of _public_repos_url is the expected
        one based on the mocked payload
        """
        mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/test-org/repos"
                }
        client = GithubOrgClient("test-org")
        result = client._public_repos_url
        expected = "https://api.github.com/orgs/test-org/repos"

        self.assertEqual(result, expected)

