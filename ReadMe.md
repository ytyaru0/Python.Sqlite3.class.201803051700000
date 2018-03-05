# このソフトウェアについて

SQLite3のトランザクション用フレームワーク。 [./src/8/](src/8/)参照。

ビジネスロジック単位を実行するたび、`begin()`,`commit()`,`engine.dispose()`する。

使いまわしているとスレッド系エラーが出るので、作ってみた。

* [問題と解法](memo/問題と解法.md)

# 開発環境

* [Raspberry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 3 Model B
    * [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) GNU/Linux 8.0 (jessie)
        * [pyenv](http://ytyaru.hatenablog.com/entry/2019/01/06/000000)
            * Python 3.6.4

# ライセンス

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)

利用ライブラリは以下。

Library|License|Copyright
-------|-------|---------
[dataset](https://dataset.readthedocs.io/en/latest/)|[MIT](https://opensource.org/licenses/MIT)|[Copyright (c) 2013, Open Knowledge Foundation, Friedrich Lindenberg, Gregor Aisch](https://github.com/pudo/dataset/blob/master/LICENSE.txt)
[SQLAlchemy](https://www.sqlalchemy.org/)|[MIT](https://opensource.org/licenses/MIT)|[Mike Bayer](https://pypi.python.org/pypi/SQLAlchemy/1.2.2)

