#!/usr/bin/env python3
"""
Module that contains the unittests for generic utilities
"""

import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function"""

    @parameterized.expand(
      [
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
      ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected)
    
    @parameterized.expand(
      [
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
      ]
    )
    def test_access_nested_map_exception(self, nested_map, path, exception):
        """Test access_nested_map function"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test get_json function"""

    @parameterized.expand(
      [
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
      ]
    )
    def test_get_json(self, url, expected_output):
        """Test get_json function"""
        with patch("utils.requests.get") as mock_get:
            mock_get.return_value.json.return_value = expected_output
            self.assertEqual(get_json(url), expected_output)