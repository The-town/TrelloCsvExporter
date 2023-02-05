# TrelloCsvExporter

指定したTrelloボード上のカード情報をCSVへ出力するためのアプリケーションです。

# 出力される情報

CSVファイルへ出力されるTrelloボード上の情報は以下になります。


| list          | name    | label           | link      |
|---------------|---------|-----------------|-----------|
| カードがあるリストの名前  | カードの名前  | カードに付与されているラベル  | カードへのリンク  |

> カードに複数のラベルがある場合は、半角スペースで区切り出力します。

# 動作環境

Pythonファイルを直接実行する場合は、Python環境（Python3.7以上）さえあれば動きます。

なお[リリースページ](https://github.com/The-town/TrelloCsvExporter/releases)に格納しているファイルは全てWindows用です。

# はじめかた

## releaseページから実行ファイルをダウンロードする

1. [リリースページ](https://github.com/The-town/TrelloCsvExporter/releases)へアクセスする。
2. **TrelloCsvExporter.exe** をダウンロードする。
3. **TrelloCsvExporter.exe** を任意のフォルダに置く。

## config.iniファイルを作成する

以下ファイルを作成して**config.ini**として保存する。

```ini
[trello-api-key]
key=TrelloのAPIキー
token=TrelloのAPIトークン

[trello-board-id]
id=TrelloのボードID
```

## 実行する

**TrelloCsvExporter.exe**ファイルを実行することで、同じフォルダにCSVファイル（output.csv）が作成される。
