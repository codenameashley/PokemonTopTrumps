#       |---------------------------|       #
#       |        **POKEAPI**        |       #
#       |     ***TOP TRUMPS***      |       #
#       |---------------------------|       #

## Importing requests for API and random
import requests
import random

## Creating a function generate a random number using random module

def randompokemonnumber():
    pokemon_number = random.randint(1, 155)
    return pokemon_number

## Function used to get pokemon card for game
def pokemoncard():
    pokeAPI= randompokemonnumber()
    pokeurl = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokeAPI)
    response = requests.get(pokeurl)
    mypokemon = response.json()
    return {'name': mypokemon['name'],
                 'id': mypokemon['id'],
                 'height': mypokemon['height'],
                 'weight': mypokemon['weight'],
                 'base_xp': mypokemon['base_experience'],
                 }
## Pokemon Card 1 from PokeAPI - Informing player of card 1 name
pokecard1 = pokemoncard()
pokecard2 = pokemoncard()
pokecard3 = pokemoncard()
print('Your 1st card is {}, your 2nd card is {}, your 3rd card is {} '.format(pokecard1['name'],pokecard2['name'], pokecard3['name']))



## Creating a function which returns stats from the chosen pokemon card
chosen_card = int(input(
        'Which card would you like to play against your opponent? Type 1 for 1st card, 2 for 2nd card, 3 for 3rd card'))

def cardforgame():
    if chosen_card == 1:
        return ('Name {}, id {}, height {}, weight {}, base experience {}'.format(pokecard1['name'],
                                                                                    pokecard1['id'],
                                                                                    pokecard1['height'],
                                                                                    pokecard1['weight'],
                                                                                    pokecard1['base_xp']))

    elif chosen_card == 2:
        return ('Name {}, id {}, height {}, weight {}, base experience {}'.format(pokecard2['name'],
                                                                                    pokecard2['id'],
                                                                                    pokecard2['height'],
                                                                                    pokecard2['weight'],
                                                                                    pokecard2['base_xp']))
    elif chosen_card == 3:
        return ('Name {}, id {}, height {}, weight {}, base experience {}'.format(pokecard3['name'],
                                                                                    pokecard3['id'],
                                                                                    pokecard3['height'],
                                                                                    pokecard3['weight'],
                                                                                    pokecard3['base_xp']))
        ## In case player inputs any number outside of 1 2 3 this code will propmt player to re-run the whole code
    else:
        return print('You need to choose a card, please run the code again and start over')

## Informing player of their chosen card's stat

print('You chose to play {}'.format(cardforgame()))


## if elif statement will return certain card and stats if a condition is satisfied
## condition is which card and stat is typed in by the player in the above functions

my_stat = input('What Stat do you want to choose? Choose between *id, height, weight, base xp* ')
def my_card_and_my_stat():
    if chosen_card == 1:
        if my_stat == 'id':
            return pokecard1['id']
    if chosen_card == 1:
        if my_stat == 'height':
            return pokecard1['height']
    if chosen_card == 1:
        if my_stat == 'weight':
            return pokecard1['weight']
    if chosen_card == 1:
        if my_stat == 'base xp':
            return pokecard1['base_xp']

    if chosen_card == 2:
        if my_stat == 'id':
            return pokecard2['id']
    if chosen_card == 2:
        if my_stat == 'height':
            return pokecard2['height']
    if chosen_card == 2:
        if my_stat == 'weight':
            return pokecard2['weight']
    if chosen_card == 2:
        if my_stat == 'base xp':
            return pokecard2['base_xp']

    if chosen_card == 3:
        if my_stat == 'id':
            return pokecard3['id']
    if chosen_card == 3:
        if my_stat == 'height':
            return pokecard3['height']
    if chosen_card == 3:
        if my_stat == 'weight':
            return pokecard3['weight']
    if chosen_card == 3:
        if my_stat == 'base xp':
            return pokecard3['base_xp']
    else:
        return print('You need to chose')


## Assigning opponent a card for this game from the 3 card deck
## Same process as above

def opponentscard():
    pokeAPI = randompokemonnumber()
    pokeurl = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokeAPI)
    response = requests.get(pokeurl)
    theirpokemon = response.json()
    return {'name': theirpokemon['name'],
            'id': theirpokemon['id'],
            'height': theirpokemon['height'],
            'weight': theirpokemon['weight'],
            'base_xp': theirpokemon['base_experience'],
            }

## Informing player of opponent's cards
oppcard1 = opponentscard()
oppcard2 = opponentscard()
oppcard3 = opponentscard()
print('Your opponents cards are {}, {}, {}'.format(oppcard1['name'], oppcard2['name'], oppcard3['name']))

## Assigning the opponent a card/stat through random generated number
## It will return a chosen card/stat when condition is satisfied

def opponents_card_and_stat():
    cardxstat = random.randint(1, 12)
    if cardxstat == 1:
        return oppcard1['id']
    elif cardxstat == 2:
        return oppcard2['id']
    elif cardxstat == 3:
        return oppcard3['id']
    elif cardxstat == 4:
        return oppcard1['height']
    elif cardxstat == 5:
        return oppcard2['height']
    elif cardxstat == 6:
        return oppcard3['height']
    elif cardxstat == 7:
        return oppcard1['weight']
    elif cardxstat == 8:
        return oppcard2['weight']
    elif cardxstat == 9:
        return oppcard3['weight']
    elif cardxstat == 10:
        return oppcard1['base_xp']
    elif cardxstat == 11:
        return oppcard2['base_xp']
    else:
        return oppcard3['base_xp']

## Assigning functions above to a variable
z = opponents_card_and_stat()
a = my_card_and_my_stat()

print('Let the battle commence!')
print('Results in')
print('3...')
print('2...')
print('1...')

## Comparing my stat to opponents randomly generated stat

if a > z:
    print('Alright! You win!')
    print('Your stat was {}, your opponents stat was {}'.format(a, z))
if a < z:
    print('You lose!')
    print('Your stat was {}, your opponents stat was {}' .format(a, z))
    print('Ill get you and your pokemon next time!')
elif a == z:
    print('Aww! Its a draw')


