# python-poetry-template

Python poetryのテンプレートリポジトリ

## Installation

```bash
poetry install

# developmentの依存関係が不要な場合
poetry isntall --no-dev
```

プロジェクト配下に`.venv`ディレクトリを作成したい場合は次の設定を有効にしてください。

```bash
poetry config virtualenvs.in-project true
```

## Usage

`main.py`は次のコマンドで実行可能です。

```bash
poetry run python src/main.py
```

以下のコマンドで`poetry`の仮想環境に入ることができます。

```bash
poetry shell
```

### Tasks

`taskipy`でタスクランナーとして次のコマンドを登録してあります。

```bash
poetry run task test
poetry run task test
poetry run task format
poetry run task lint
poetry run task docs
```
