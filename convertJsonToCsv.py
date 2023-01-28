import csv
import json
from typing import List

from getTrelloBoard import get_cards_on_trello_board, get_lists_on_trello_board

output_path: str = "output.csv"

row_data_list: List = []

trello_lists: dict = {trello_list["id"]: trello_list["name"] for trello_list in get_lists_on_trello_board()}

for card in get_cards_on_trello_board():
    row_data: dict = {
        "list": trello_lists[card["idList"]],
        "name": card["name"],
        "label": " ".join([label["name"] for label in card["labels"]]),
        "link": card['url']
    }
    row_data_list.append(row_data)


with open(output_path, "w", encoding="utf-8", newline="") as f:
    writer: csv.DictWriter = csv.DictWriter(f, row_data_list[0].keys())
    writer.writeheader()
    writer.writerows(row_data_list)
