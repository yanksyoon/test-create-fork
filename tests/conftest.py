# Copyright 2024 Canonical Ltd.
# See LICENSE file for licensing details.

"""Fixtures for github runner charm."""


from pytest import Parser


def pytest_addoption(parser: Parser):
    """Add options to pytest parser."""
    parser.addoption("--path", action="store")
    parser.addoption("--token", action="store")
    parser.addoption(
        "--tokens",
        action="store",
        help=(
            "A comma separated GitHub Personal Access Token(s). "
            "Add more than one to help reduce rate limiting."
        ),
    )
    parser.addoption("--charm-file", action="store")
    parser.addoption("--token-alt", action="store")
    parser.addoption("--http-proxy", action="store")
    parser.addoption("--https-proxy", action="store")
    parser.addoption("--no-proxy", action="store")
    parser.addoption("--loop-device", action="store")
