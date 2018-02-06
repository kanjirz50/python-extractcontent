ExtractContent3
===============

.. image:: https://img.shields.io/pypi/v/extractcontent3.svg
    :target: https://pypi.python.org/pypi/extractcontent3

.. image:: https://img.shields.io/pypi/l/extractcontent3.svg
    :target: https://pypi.python.org/pypi/extractcontent3

.. image:: https://img.shields.io/pypi/pyversions/extractcontent3.svg
    :target: https://pypi.python.org/pypi/extractcontent3

.. image:: https://travis-ci.org/kanjirz50/python-extractcontent3.svg?branch=master
    :target: https://travis-ci.org/kanjirz50/python-extractcontent3

ExtractContent3はPython3で動作する、HTMLから本文を抽出するモジュールです。
このモジュールは、ExtractContent RubyモジュールをPython用に書き直したpython-extracontentを改造したものです。

Usage
------------

.. code-block:: python

   from extractcontent3 import ExtractContent
   extractor = ExtractContent()

   # オプション値を指定する
   opt = {"threshold":50}
   extractor.set_default(opt)

   html = open("index.html").read() # 解析対象HTML
   extractor.analyse(html)
   text, title = extractor.as_text()
   html, title = extractor.as_html()
   title = extractor.extract_title(html)

Installation
------------

.. code-block:: bash

   # pypi
   $ pip install extractcontent3
   
   # Githubからのインストール
   $ pip install git+https://github.com/kanjirz50/python-extractcontent3

Option
-------------

.. code-block:: python

   """
   オプションの種類:
   名称 / デフォルト値
   
   threshold / 100
   本文と見なすスコアの閾値

   min_length / 80
   評価を行うブロック長の最小値

   decay_factor / 0.73
   減衰係数
   小さいほど先頭に近いブロックのスコアが高くなります

   continuous_factor / 1.62
   連続ブロック係数
   大きいほどブロックを連続と判定しにくくなる

   punctuation_weight / 10
   句読点に対するスコア　
   大きいほど句読点が存在するブロックを本文と判定しやすくなる

   punctuations r"(?is)([\u3001\u3002\uff01\uff0c\uff0e\uff1f]|\.[^A-Za-z0-9]|,[^0-9]|!|\?)"    
   句読点を抽出する正規表現
    
   waste_expressions / r"(?i)Copyright|All Rights Reserved"
   フッターに含まれる特徴的なキーワードを指定した正規表現

   debug / False
    Trueの場合、ブロック情報を出力
   """

謝辞
----

オリジナル版の作成者やForkで改良を加えた方々に感謝します。

- Copyright of the original implementation:: (c)2007/2008/2009 Nakatani Shuyo / Cybozu labs Inc. All rights reserved
  - http://rubyforge.org/projects/extractcontent/
  - http://labs.cybozu.co.jp/blog/nakatani/2007/09/web_1.html
- https://github.com/petitviolet/python-extractcontent
- https://github.com/yono/python-extractcontent
