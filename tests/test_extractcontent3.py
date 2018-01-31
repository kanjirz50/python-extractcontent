"""
Test
"""

import pytest
from extractcontent3 import ExtractContent

class TestExtractContent(object):
    @pytest.fixture()
    def extract_content():
        return ExtractContent()

    def test_100(self):
        pass
