#!/usr/bin/env python3
"""
Module providing unit test for GitHub organization client
"""

import unittest
from client import GithubOrgClient
from requests import HTTPError
from fixtures import TEST_PAYLOAD
from unittest.mock import (
    patch,
    Mock,
    MagicMock,
    PropertyMock,
)
from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """Unit test for GitHub organization client"""

    @parameterized.expand(
        [
            ("google", {'login': "google"}),
            ("abc", {'login': "abc"}),
        ]
    )
    @patch("client.get_json")
    def test_org(self, org_name: str, expected_url: dict,
                 mock_get_json: MagicMock) -> None:
        """Test org function"""
        mock_get_json.return_value = MagicMock(return_value=TEST_PAYLOAD)

        org = GithubOrgClient(org_name)

        self.assertEqual(org.org, expected_url)

        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org_name))

    def test_public_repos_url(self):
        """Test public_repos_url function"""
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock) \
                as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/google/repos"
            }

            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/orgs/g  oogle/repos"
            )

    @patch("client.get_json")
    @patch.object(GithubOrgClient, '_public_repos_url',
                  new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test public_repos function"""
        payload = [
            {"name": "repo1", "license": {"key": "MIT"}},
            {"name": "repo2", "license": {"key": "Apache"}},
            {"name": "repo3", "license": {"key": "GPL"}},
        ]

        mock_get_json.return_value = payload

        mock_public_repos_url.return_value = \
            "https://api.github.com/orgs/example/repos"

        client = GithubOrgClient("example")

        repos = client.public_repos()

        self.assertEqual(repos, ["repo1", "repo2", "repo3"])

        mock_get_json.assert_called_once()

        mock_public_repos_url.assert_called_once()