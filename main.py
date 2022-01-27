import os
import requests
import json


def main():
        
    token = os.environ['INPUT_TOKEN']
    api_key = os.environ['INPUT_API_KEY']
    if token == "" or api_key == "":
        raise Exception("API_KEY and TOKEN required")

    list_id = os.environ['INPUT_LIST_ID']
    
    if list_id == "":
        list_name = os.environ['INPUT_LIST_NAME']
        board_id = os.environ['INPUT_BOARD_ID']
        # Get list_id by list_name and board_id
        if list_name != "" and board_id != "":
            url_board = f"https://api.trello.com/1/boards/{board_id}/lists"
            querystring = {"key": api_key,
                "token": token}
            res_board = requests.request("GET", url_board, params=querystring)
            lists = json.loads(res_board.text)
            for column in lists:
                if column['name'] == list_name:
                    list_id = column['id']
                    break

    querystring = {
        "name": os.environ['INPUT_CARD_NAME'],
        "desc": os.environ['INPUT_CARD_DESCRIPTION'],
        "pos": "top",
        "idList": list_id,
        "key": api_key,
        "token": token
    }
    url_add_card = "https://api.trello.com/1/cards"
    res_board = requests.request("POST", url_add_card, params=querystring)
    print(json.loads(res_board.text))


if __name__ == '__main__':
    main()
