print('Welcome to Blackjack, thanks for playing')
print('----------------------------------------')
print('Shuffle up and deal!')
print('----------------------------------------')

#using an API get request to import 6 decks of cards
import requests
shuffleurl='https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=6'
resp_shuffle=requests.get(shuffleurl)
deck=resp_shuffle.json()
deck_id= deck["deck_id"]
print(deck_id)

#using a post API to draw from the deck
drawurl= f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=3'
resp_draw=requests.post(drawurl)
print(resp_draw.status_code)
cards_drawn=resp_draw.json()
print(cards_drawn)

#or using a dictionary defined within the code
deck=[
    {"suit": 'clubs', "card": 'Ace',"value": [ 1, 10 ]},
    {"suit": 'clubs', "card": '2', "value": 2 },
    {"suit": 'clubs', "card": '3', "value": 3 },
    {"suit": 'clubs', "card": '4', "value": 4 },
    {"suit": 'clubs', "card": '5', "value": 5 },
    {"suit": 'clubs', "card": '6', "value": 6 },
    {"suit": 'clubs', "card": '7', "value": 7 },
    {"suit": 'clubs', "card": '8', "value": 8 },
    {"suit": 'clubs', "card": '9', "value": 9 },
    {"suit": 'clubs', "card": '10', "value": 10 },
    {"suit": 'clubs', "card": 'Jack', "value": 10 },
    {"suit": 'clubs', "card": 'Queen', "value": 10 },
    {"suit": 'clubs', "card": 'King', "value": 10 },

     {"suit": 'diamonds', "card": 'Ace', "value": [ 1, 10 ] },
     {"suit": 'diamonds', "card": '2', "value": 2 },
     {"suit": 'diamonds', "card": '3', "value": 3 },
     {"suit": 'diamonds', "card": '4', "value": 4 },
     {"suit": 'diamonds', "card": '5', "value": 5 },
     {"suit": 'diamonds', "card": '6', "value": 6 },
     {"suit": 'diamonds', "card": '7', "value": 7 },
     {"suit": 'diamonds', "card": '8', "value": 8 },
     {"suit": 'diamonds', "card": '9', "value": 9 },
     {"suit": 'diamonds', "card": '10', "value": 10 },
     {"suit": 'diamonds', "card": 'Jack', "value": 10 },
     {"suit": 'diamonds', "card": 'Queen', "value": 10 },
     {"suit": 'diamonds', "card": 'King', "value": 10 },

     {"suit": 'hearts', "card": 'Ace', "value": [ 1, 10 ] },
     {"suit": 'hearts', "card": '2', "value": 2 },
     {"suit": 'hearts', "card": '3', "value": 3 },
     {"suit": 'hearts', "card": '4', "value": 4 },
     {"suit": 'hearts', "card": '5', "value": 5 },
     {"suit": 'hearts', "card": '6', "value": 6 },
     {"suit": 'hearts', "card": '7', "value": 7 },
     {"suit": 'hearts', "card": '8', "value": 8 },
     {"suit": 'hearts', "card": '9', "value": 9 },
     {"suit": 'hearts', "card": '10', "value": 10 },
     {"suit": 'hearts', "card": 'Jack', "value": 10 },
     {"suit": 'hearts', "card": 'Queen', "value": 10 },
     {"suit": 'hearts', "card": 'King', "value": 10 },

     {"suit": 'spades', "card": 'Ace', "value": [ 1, 10 ] },
     {"suit": 'spades', "card": '2', "value": 2 },
     {"suit": 'spades', "card": '3', "value": 3 },
     {"suit": 'spades', "card": '4', "value": 4 },
     {"suit": 'spades', "card": '5', "value": 5 },
     {"suit": 'spades', "card": '6', "value": 6 },
     {"suit": 'spades', "card": '7', "value": 7 },
     {"suit": 'spades', "card": '8', "value": 8 },
     {"suit": 'spades', "card": '9', "value": 9 },
     {"suit": 'spades', "card": '10', "value": 10 },
     {"suit": 'spades', "card": 'Jack', "value": 10 },
     {"suit": 'spades', "card": 'Queen', "value": 10 },
     {"suit": 'spades', "card": 'King', "value": 10 }
]