[![GitHub license](https://img.shields.io/github/license/TrisNol/trello-create-card-action.svg)](https://github.com/TrisNol/trello-create-card-action/blob/master/LICENSE)
[![GitHub forks](https://img.shields.io/github/forks/TrisNol/trello-create-card-action.svg?style=social&label=Fork&maxAge=2592000)](https://github.com/TrisNol/trello-create-card-action)
[![GitHub stars](https://img.shields.io/github/stars/TrisNol/trello-create-card-action?style=social&label=Star&maxAge=2592000)](https://GitHub.com/TrisNol/trello-create-card-action/stargazers/)

# Trello Create Card Action
This repo contains a GitHub Action for creating Trello cards automatically.

## How to use
The action has two modes of operation: It can either use a given ```list_id```, which identifies the list of a board, or it will determine the ```list_id``` itself by identifying it based on the list´s name.

If the ```list_id``` is not provided, the ```board_id``` and ```list_name``` have to be present:
```yml      
    - name: Create a Trello Card
      uses: TrisNol/trello-create-card-action@main
      with:
        api_key: ${{ secrets.TRELLO_API_KEY }}
        token: ${{ secrets.TRELLO_TOKEN }}
        board_id: "e44b6oBU"
        list_name: "To Do"
        card_name: "I´m a test card"
        card_description: "I´m the card´s description"
```

You do not have to provide the ```card_name``` or ```card_description``` manually, insted the information provided in different workflows (e.g. for pull requests) can be utilized:

```yml      
    - name: Create a Trello Card
      uses: TrisNol/trello-create-card-action@main
      with:
        api_key: ${{ secrets.TRELLO_API_KEY }}
        token: ${{ secrets.TRELLO_TOKEN }}
        board_id: "e44b6oBU"
        list_name: "To Do"
        card_name: ${{ github.event.pull_request.title }}
        card_description: ${{ github.repositoryUrl }}
```
