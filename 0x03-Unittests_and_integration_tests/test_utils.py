#!/usr/bin/env python3

'''Module for testing utils file'''
from parameterized import parameterized
import unittest
from utils import (access_nested_map, get_json)
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Class for testing access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test the return value returns what is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test for KeyError if it's raised for the respactive input"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(f"KeyError('{expected}')", repr(e.exception))


class TestGetJson(unittest.TestCase):
    """Class for testing get_json method"""
    @patch('requests.get')
    def test_get_json(self, mock_get):
        """Test for the get_json method if it returns the expected result"""
        test_cases = [
                ("http://example.com", {"payload": True}),
                ("http://holberton.io", {"payload": False})
                ]
        for test_url, test_payload in test_cases:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)
            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)
            mock_get.reset_mock()
