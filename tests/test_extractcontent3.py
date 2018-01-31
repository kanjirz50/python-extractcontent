"""
Test
"""

import pytest
from extractcontent3 import ExtractContent

class TestExtractContentHatenaBlog(object):
    @pytest.fixture()
    def extractor(self):
        html = open("./tests/blog.html").read()
        extractor = ExtractContent()
        extractor.analyse(html)
        return extractor

    def test_text(self, extractor):
        text, title = extractor.as_text()
        assert text.strip().startswith("【Xonsh Advent Calendar 2017の13日目の記事です。】")

    def test_title(self, extractor):
        text, title = extractor.as_text()
        assert title == "Xonshを使ってみた - かんちゃんの備忘録"
