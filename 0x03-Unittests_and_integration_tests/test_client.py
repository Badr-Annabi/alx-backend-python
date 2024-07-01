#!/usr/bin/env python3
"""Module for testing client"""


from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch


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
