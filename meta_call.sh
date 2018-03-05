#!/bin/bash
user=ytyaru0
desc="SQLite3のトランザクション用フレームワーク。メモ追記"
url=http://ytyaru.hatenablog.com/entry/2019/02/01/000000
target=$(cd $(dirname $0) && pwd)

. /home/pi/root/script/sh/pyenv.sh
. /home/pi/root/env/py/auto_github/bin/activate

script=/tmp/work/GitHub.Uploader.Pi3.Https.201802210700/src/Uploader.py
python3 ${script} "${target}" -u  "${user}" -d "${desc}" -l "${url}"

