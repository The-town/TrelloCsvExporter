import json
import requests

import config


def get_cards_on_trello_board() -> list:
    """
    Trelloボード上にある全てのカードを取得する関数

    Returns
    --------
    r.json(): list
        カードの情報
    """
    payload: dict = {
        "key": config.rule_file["trello-api-key"]["key"],
        "token": config.rule_file["trello-api-key"]["token"]
    }

    r = requests.get(f"https://api.trello.com/1/boards/{config.rule_file['trello-board-id']['id']}/cards", payload)
    return r.json()


def get_lists_on_trello_board() -> list:
    """
    Trelloボード上にある全てのリストを取得する関数

    Returns
    --------
    r.json(): dict
        リストの情報
    """
    payload: dict = {
        "key": config.rule_file["trello-api-key"]["key"],
        "token": config.rule_file["trello-api-key"]["token"]
    }

    r = requests.get(f"https://api.trello.com/1/boards/{config.rule_file['trello-board-id']['id']}/lists", payload)
    return r.json()
