#       |---------------------------|       #
#       |        **POKEAPI**        |       #
#       |     ***TOP TRUMPS***      |       #
#       |---------------------------|       #


f = open('PokeScores.txt', 'w')


import requests
import random

playername = input('Welcome to the battle arena, trainer!\n'
                   'What is your name?\n')

playergym = input('What gym or team do you belong to?\n')

q = playername
r = playergym

print('Battle Master: "A new contender has entered the arena!')

def opponent():
    i = random.randint(1, 5)
    if i == 1:
        return 'Ash'
    elif i == 2:
        return 'Misty'
    elif i == 3:
        return 'Jessie'
    elif i == 4:
        return 'James'
    else:
        return 'Brock'

opponent()

l = opponent()

def gym():
    if l == 'Ash':
        return 'Aether Foundation'
    elif l == 'Misty':
        return 'Cerulean Gym'
    elif l == 'Jessie':
        return 'Team Rocket'
    elif l == 'James':
        return 'Team Rocket'
    else:
        return 'Pewter Gym'

gym()

m = gym()

print('Battle Master: "Your opponent for this battle is {} of {}"\n'.format(l, m))
print(
    'Battle Master: "The rules of this battle arena are - \n '
    '1. You choose a pokemon to battle against the opponent\n '
    '2. Choose between the 4 stats to compare against your opponent\n ' 
    '3. The trainer with the highest stat wins the round!\n '
    '4. There are 3 rounds in the championship, whoever wins 2 rounds will be the battle arena champion!"\n')

print('Battle Master: "{} from {} is ready to battle!"\n'.format(q, r))

def randompokemonnumber():
    pokemon_number = random.randint(1, 155)
    return pokemon_number

randompokemonnumber()

def pokemoncard():
    pokeAPI = randompokemonnumber()
    pokeurl = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokeAPI)
    response = requests.get(pokeurl)
    mypokemon = response.json()
    return {'name': mypokemon['name'],
            'id': mypokemon['id'],
            'height': mypokemon['height'],
            'weight': mypokemon['weight'],
            'base_xp': mypokemon['base_experience'],
            }

pokemoncard()

pokecard1 = pokemoncard()
pokecard2 = pokemoncard()
pokecard3 = pokemoncard()
pokecard4 = pokemoncard()
pokecard5 = pokemoncard()

print('Battle Master: "I see you brought 5 pokemons with you for this battle"\n')

print('*You check your bag and see 5 pokeballs, your Pokedex will provide you with stats*')

pokeballs = ('Pokedex: "Pokeball 1 contains {}, Pokeball 2 contains {}, Pokeball 3 contains {}, Pokeball 4 contains {}, Pokeball 5 contains {}"\n').format(pokecard1['name'],
                                                                                                                        pokecard2['name'],
                                                                                                                        pokecard3['name'],
                                                                                                                        pokecard4['name'],
                                                                                                                        pokecard5['name'])

print(pokeballs)

print('         **ROUND 1**           \n')

print('*Preparation stage*\n')

chosen_card1 = int(input(
    'Pokedex: "Which pokemon would you like to play against {}? Type 1 for {}, 2 for {}, 3 for {}, 4 for {}, 5 for {}"\n'.format(
        l, pokecard1['name'],
        pokecard2['name'],
        pokecard3['name'],
        pokecard4['name'],
        pokecard5['name'])))

def cardforgame1():
    if chosen_card1 == 1:
        return ('{},\nid {},\nheight {},\nweight {},\nbase experience {}'.format(pokecard1['name'],
                                                                                 pokecard1['id'],
                                                                                 pokecard1['height'],
                                                                                 pokecard1['weight'],
                                                                                 pokecard1['base_xp']))

    elif chosen_card1 == 2:
        return ('{},\nid {},\nheight {},\nweight {},\nbase experience {}'.format(pokecard2['name'],
                                                                                 pokecard2['id'],
                                                                                 pokecard2['height'],
                                                                                 pokecard2['weight'],
                                                                                 pokecard2['base_xp']))
    elif chosen_card1 == 3:
        return ('{},\nid {},\nheight {},\nweight {},\nbase experience {}'.format(pokecard3['name'],
                                                                                 pokecard3['id'],
                                                                                 pokecard3['height'],
                                                                                 pokecard3['weight'],
                                                                                 pokecard3['base_xp']))
    elif chosen_card1 == 4:
        return ('{},\nid {},\nheight {},\nweight {},\nbase experience {}'.format(pokecard4['name'],
                                                                                 pokecard4['id'],
                                                                                 pokecard4['height'],
                                                                                 pokecard4['weight'],
                                                                                 pokecard4['base_xp']))
    elif chosen_card1 == 5:
        return ('{},\nid {},\nheight {},\nweight {},\nbase experience {}'.format(pokecard5['name'],
                                                                                 pokecard5['id'],
                                                                                 pokecard5['height'],
                                                                                 pokecard5['weight'],
                                                                                 pokecard5['base_xp']))
        ## In case player inputs any number outside of 1 2 3 this code will propmt player to re-run the whole code
    else:
        return print('Battle Master: "You need to choose a pokemon! You cant go into battle without one!"')


cardforgame1()

print('\nPokedex: "{} chose to play {}"'.format(q, cardforgame1()))

my_stat1 = input(
    '\nPokedex: "Which stat would you like to play against {}? Choose between *id, height, weight, base xp*"\n'.format(l))

def my_card_and_my_stat1():
    if chosen_card1 == 1:
        if my_stat1 == 'id':
            return pokecard1['id']
    if chosen_card1 == 1:
        if my_stat1 == 'height':
            return pokecard1['height']
    if chosen_card1 == 1:
        if my_stat1 == 'weight':
            return pokecard1['weight']
    if chosen_card1 == 1:
        if my_stat1 == 'base xp':
            return pokecard1['base_xp']
    if chosen_card1 == 2:
        if my_stat1 == 'id':
            return pokecard2['id']
    if chosen_card1 == 2:
        if my_stat1 == 'height':
            return pokecard2['height']
    if chosen_card1 == 2:
        if my_stat1 == 'weight':
            return pokecard2['weight']
    if chosen_card1 == 2:
        if my_stat1 == 'base xp':
            return pokecard2['base_xp']
    if chosen_card1 == 3:
        if my_stat1 == 'id':
            return pokecard3['id']
    if chosen_card1 == 3:
        if my_stat1 == 'height':
            return pokecard3['height']
    if chosen_card1 == 3:
        if my_stat1 == 'weight':
            return pokecard3['weight']
    if chosen_card1 == 3:
        if my_stat1 == 'base xp':
            return pokecard3['base_xp']
    if chosen_card1 == 4:
        if my_stat1 == 'id':
            return pokecard4['id']
    if chosen_card1 == 4:
        if my_stat1 == 'height':
            return pokecard4['height']
    if chosen_card1 == 4:
        if my_stat1 == 'weight':
            return pokecard4['weight']
    if chosen_card1 == 4:
        if my_stat1 == 'base xp':
            return pokecard4['base_xp']
    if chosen_card1 == 5:
        if my_stat1 == 'id':
            return pokecard5['id']
    if chosen_card1 == 5:
        if my_stat1 == 'height':
            return pokecard5['height']
    if chosen_card1 == 5:
        if my_stat1 == 'weight':
            return pokecard5['weight']
    if chosen_card1 == 5:
        if my_stat1 == 'base xp':
            return pokecard5['base_xp']
    else:
        return print('Battle Master: "You need to choose a stat from your chosen pokemon!"')

my_card_and_my_stat1()

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

opponentscard()


oppcard1 = opponentscard()
oppcard2 = opponentscard()
oppcard3 = opponentscard()
oppcard4 = opponentscard()
oppcard5 = opponentscard()

def randomoppcard():
    j = random.randint(1, 6)
    if j == 1:
        return oppcard1['name'], oppcard1['id'], oppcard1['height'], oppcard1['weight'], oppcard1['base_xp']
    elif j == 2:
        return oppcard2['name'], oppcard2['id'], oppcard2['height'], oppcard2['weight'], oppcard2['base_xp']
    elif j == 3:
        return oppcard3['name'], oppcard3['id'], oppcard3['height'], oppcard3['weight'], oppcard3['base_xp']
    elif j == 4:
        return oppcard4['name'], oppcard4['id'], oppcard4['height'], oppcard4['weight'], oppcard4['base_xp']
    else:
        return oppcard5['name'], oppcard5['id'], oppcard5['height'], oppcard5['weight'], oppcard5['base_xp']
randomoppcard()

k = randomoppcard()

def opponents_card_and_stat1():
    k = random.randint(1, 6)
    if k == 1:
        if my_stat1 == 'id':
            return oppcard1['id']
    if k == 1:
        if my_stat1 == 'height':
            return oppcard1['height']
    if k == 1:
        if my_stat1 == 'weight':
            return oppcard1['weight']
    if k == 1:
        if my_stat1 == 'base xp':
            return oppcard1['base_xp']

    if k == 2:
        if my_stat1 == 'id':
            return oppcard2['id']
    if k == 2:
        if my_stat1 == 'height':
            return oppcard2['height']
    if k == 2:
        if my_stat1 == 'weight':
            return oppcard2['weight']
    if k == 2:
        if my_stat1 == 'base xp':
            return oppcard2['base_xp']

    if k == 3:
        if my_stat1 == 'id':
            return oppcard3['id']
    if k == 3:
        if my_stat1 == 'height':
            return oppcard3['height']
    if k == 3:
        if my_stat1 == 'weight':
            return oppcard3['weight']
    if k == 3:
        if my_stat1 == 'base xp':
            return oppcard3['base_xp']

    if k == 4:
        if my_stat1 == 'id':
            return oppcard4['id']
    if k == 4:
        if my_stat1 == 'height':
            return oppcard4['height']
    if k == 4:
        if my_stat1 == 'weight':
            return oppcard4['weight']
    if k == 4:
        if my_stat1 == 'base xp':
            return oppcard4['base_xp']

    if k == 5:
        if my_stat1 == 'id':
            return oppcard5['id']
    if k == 5:
        if my_stat1 == 'height':
            return oppcard5['height']
    if k == 5:
        if my_stat1 == 'weight':
            return oppcard5['weight']
    if k == 5:
        if my_stat1 == 'base xp':
            return oppcard5['base_xp']
opponents_card_and_stat1()

print('         **BATTLE STAGE**            \n')

print('Battle Master: "{} and {} are ready! Let the battle commence!"\nResults in 3... 2... 1...\n'.format(q, l))

def results1():
    z = opponents_card_and_stat1()
    a = my_card_and_my_stat1()
    if a > z:
        with open('PokeScores.txt', 'a') as myfile:
            myfile.write('Player ' + str(1))
        print(
            '\nBattle Master: "Alright! {} wins round 1! \nYour stat was {}, {}s stat was {}"\n{} says: "Ill get you and your pokemon next time!"'.format(
                q, a, l, z, l))
    if a < z:
        with open('PokeScores.txt', 'a') as myfile:
            myfile.write('Opponent ' + str(1))
        print(
            '\nBattle Master "You lose! {} wins round 1! \nYour stat was {}, {}s stat was {}"\n{} says "Better luck next time trainer!"'.format(
                l, a, l, z, l))
    elif a == z:
        print('\nAww! Its a draw')

results1()

def scoringquotes1():
    with open('PokeScores.txt') as myfile:
        for line in myfile:
            if 'Player ' + str(1) in line:
             print(
                '\nBattle Master: "The battle is heating up after round 1! \nits {} who makes it on to the score board"\n{} says: "Dont get too comfy rookie this is just the start"'.format(
                    q, l))
            elif 'Opponent ' + str(1) in line:
                print(
                    '\nBattle Master"{} makes it to the score board!"\n{} says: "Youve got nothing on my Pokemon!"'.format(
                    l, l))
scoringquotes1()

print('\n         **ROUND 2**         \n')

randompokemonnumber()

pokemoncard()

print('PREPARATION STAGE\n')

print('Pokedex: "Your current pokemons are -\n{}"'.format(pokeballs))

chosen_card2 = int(input(
    'Pokedex "Which pokemon would you like to play against {}? Type 1 for {}, 2 for {}, 3 for {}, 4 for {}, 5 for {}"\n'.format(
        l, pokecard1['name'],
        pokecard2['name'],
        pokecard3['name'],
        pokecard4['name'],
        pokecard5['name'],)))

def cardforgame2():
    if chosen_card2 == 1:
        return ('{},\nid {},\nheight {},\nweight {},\nbase experience {}'.format(pokecard1['name'],
                                                                                 pokecard1['id'],
                                                                                 pokecard1['height'],
                                                                                 pokecard1['weight'],
                                                                                 pokecard1['base_xp']))

    elif chosen_card2 == 2:
        return ('{},\nid {},\nheight {},\nweight {},\nbase experience {}'.format(pokecard2['name'],
                                                                                 pokecard2['id'],
                                                                                 pokecard2['height'],
                                                                                 pokecard2['weight'],
                                                                                 pokecard2['base_xp']))
    elif chosen_card2 == 3:
        return ('{},\nid {},\nheight {},\nweight {},\nbase experience {}'.format(pokecard3['name'],
                                                                                 pokecard3['id'],
                                                                                 pokecard3['height'],
                                                                                 pokecard3['weight'],
                                                                                 pokecard3['base_xp']))
    elif chosen_card2 == 4:
        return ('{},\nid {},\nheight {},\nweight {},\nbase experience {}'.format(pokecard4['name'],
                                                                                 pokecard4['id'],
                                                                                 pokecard4['height'],
                                                                                 pokecard4['weight'],
                                                                                 pokecard4['base_xp']))
    elif chosen_card2 == 5:
        return ('{},\nid {},\nheight {},\nweight {},\nbase experience {}'.format(pokecard5['name'],
                                                                                 pokecard5['id'],
                                                                                 pokecard5['height'],
                                                                                 pokecard5['weight'],
                                                                                 pokecard5['base_xp']))
        ## In case player inputs any number outside of 1 2 3 this code will propmt player to re-run the whole code
    else:
        return print('Battle Master: "You need to choose a pokemon! You cant go into battle without one!"')

cardforgame2()

print('\nPokedex: "You chose to play {}"'.format(cardforgame2()))

my_stat2 = input(
    '\nPokedex: "Which stat would you like to play against {}? Choose between *id, height, weight, base xp*"\n'.format(l))

def my_card_and_my_stat2():
    if chosen_card2 == 1:
        if my_stat2 == 'id':
            return pokecard1['id']
    if chosen_card2 == 1:
        if my_stat2 == 'height':
            return pokecard1['height']
    if chosen_card2 == 1:
        if my_stat2 == 'weight':
            return pokecard1['weight']
    if chosen_card2 == 1:
        if my_stat2 == 'base xp':
            return pokecard1['base_xp']
    if chosen_card2 == 2:
        if my_stat2 == 'id':
            return pokecard2['id']
    if chosen_card2 == 2:
        if my_stat2 == 'height':
            return pokecard2['height']
    if chosen_card2 == 2:
        if my_stat2 == 'weight':
            return pokecard2['weight']
    if chosen_card2 == 2:
        if my_stat2 == 'base xp':
            return pokecard2['base_xp']
    if chosen_card2 == 3:
        if my_stat2 == 'id':
            return pokecard3['id']
    if chosen_card2 == 3:
        if my_stat2 == 'height':
            return pokecard3['height']
    if chosen_card2 == 3:
        if my_stat2 == 'weight':
            return pokecard3['weight']
    if chosen_card2 == 3:
        if my_stat2 == 'base xp':
            return pokecard3['base_xp']
    if chosen_card2 == 4:
        if my_stat2 == 'id':
            return pokecard4['id']
    if chosen_card2 == 4:
        if my_stat2 == 'height':
            return pokecard4['height']
    if chosen_card2 == 4:
        if my_stat2 == 'weight':
            return pokecard4['weight']
    if chosen_card2 == 4:
        if my_stat2 == 'base xp':
            return pokecard4['base_xp']
    if chosen_card2 == 5:
        if my_stat2 == 'id':
            return pokecard5['id']
    if chosen_card2 == 5:
        if my_stat2 == 'height':
            return pokecard5['height']
    if chosen_card2 == 5:
        if my_stat2 == 'weight':
            return pokecard5['weight']
    if chosen_card2 == 5:
        if my_stat2 == 'base xp':
            return pokecard5['base_xp']
    else:
        return print('Battle Master: "You need to choose a stat from your chosen pokemon!"')
my_card_and_my_stat2()

opponentscard()

def opponents_card_and_stat2():
    k = random.randint(1, 6)
    if k == 1:
        if my_stat2 == 'id':
            return oppcard1['id']
    if k == 1:
        if my_stat2 == 'height':
            return oppcard1['height']
    if k == 1:
        if my_stat2 == 'weight':
            return oppcard1['weight']
    if k == 1:
        if my_stat2 == 'base xp':
            return oppcard1['base_xp']

    if k == 2:
        if my_stat2 == 'id':
            return oppcard2['id']
    if k == 2:
        if my_stat2 == 'height':
            return oppcard2['height']
    if k == 2:
        if my_stat2 == 'weight':
            return oppcard2['weight']
    if k == 2:
        if my_stat2 == 'base xp':
            return oppcard2['base_xp']

    if k == 3:
        if my_stat2 == 'id':
            return oppcard3['id']
    if k == 3:
        if my_stat2 == 'height':
            return oppcard3['height']
    if k == 3:
        if my_stat2 == 'weight':
            return oppcard3['weight']
    if k == 3:
        if my_stat2 == 'base xp':
            return oppcard3['base_xp']

    if k == 4:
        if my_stat2 == 'id':
            return oppcard4['id']
    if k == 4:
        if my_stat2 == 'height':
            return oppcard4['height']
    if k == 4:
        if my_stat2 == 'weight':
            return oppcard4['weight']
    if k == 4:
        if my_stat2 == 'base xp':
            return oppcard4['base_xp']

    if k == 5:
        if my_stat2 == 'id':
            return oppcard5['id']
    if k == 5:
        if my_stat2 == 'height':
            return oppcard5['height']
    if k == 5:
        if my_stat2 == 'weight':
            return oppcard5['weight']
    if k == 5:
        if my_stat2 == 'base xp':
            return oppcard5['base_xp']

opponents_card_and_stat2()

print('Battle Master: "Round 2! FIGHT!"\nResults in 3... 2... 1...')

def results2():
    b = my_card_and_my_stat2()
    t = opponents_card_and_stat2()
    if b > t:
        with open('PokeScores.txt', 'a') as myfile:
            myfile.write('Player ' + str(2))
        print(
            '\nBattle Master: "Alright! {} wins round 2!\nYour stat was {}, {}s stat was {}"\n{} says: "Theres no way I lost that round!"'.format(
                q, b, l, t, l))
    if b < t:
        with open('PokeScores.txt', 'a') as myfile:
            myfile.write('Opponent ' + str(2))
        print(
            '\nBattle Master: "You lose! {} wins round 2!\nYour stat was {}, {}s stat was {}"\n{} says "Its all down to the final round! May the best trainer win!"'.format(
                l, b, l, t, l))
    elif b == t:
        print('\nAww! Its a draw')

results2()

def scoringquotes2():
    with open('PokeScores.txt') as myfile:
        for line in myfile:
            if 'Player ' + str(2) in line:
             print(
                '\nBattle Master "WOW! What a round!\n{} takes the lead!!!"\n{} says: "I cant let you win!"'.format(
                    q, l))
            elif 'Opponent ' + str(2) in line:
                print(
                    '\nBattle Master: "Its {} who takes the lead!"\n {} says: "Its that all youve got?!"'.format(
                    l, l))
scoringquotes2()

print('\n             **ROUND 3 - FINAL ROUND**            \n')

randompokemonnumber()

pokemoncard()

print('PREPARATION STAGE\n')

print('Pokedex: "Your current pokemons are - {}"'.format(pokeballs))

chosen_card3 = int(input(
    'Pokedex: "Which pokemon would you like to play against {}? Type 1 for {}, 2 for {}, 3 for {}, 4 for {}, 5 for {}'
    'This is the final round, choose wisely"\n'.format(
        l, pokecard1['name'],
        pokecard2['name'],
        pokecard3['name'],
        pokecard4['name'],
        pokecard5['name'])))

def cardforgame3():
    if chosen_card3 == 1:
        return ('{},\nid {},\nheight {},\nweight {},\nbase experience {}'.format(pokecard1['name'],
                                                                                 pokecard1['id'],
                                                                                 pokecard1['height'],
                                                                                 pokecard1['weight'],
                                                                                 pokecard1['base_xp']))

    elif chosen_card3 == 2:
        return ('{},\nid {},\nheight {},\nweight {},\nbase experience {}'.format(pokecard2['name'],
                                                                                 pokecard2['id'],
                                                                                 pokecard2['height'],
                                                                                 pokecard2['weight'],
                                                                                 pokecard2['base_xp']))
    elif chosen_card3 == 3:
        return ('{},\nid {},\nheight {},\nweight {},\nbase experience {}'.format(pokecard3['name'],
                                                                                 pokecard3['id'],
                                                                                 pokecard3['height'],
                                                                                 pokecard3['weight'],
                                                                                 pokecard3['base_xp']))
    elif chosen_card3 == 4:
        return ('{},\nid {},\nheight {},\nweight {},\nbase experience {}'.format(pokecard4['name'],
                                                                                 pokecard4['id'],
                                                                                 pokecard4['height'],
                                                                                 pokecard4['weight'],
                                                                                 pokecard4['base_xp']))
    elif chosen_card3 == 5:
        return ('{},\nid {},\nheight {},\nweight {},\nbase experience {}'.format(pokecard5['name'],
                                                                                 pokecard5['id'],
                                                                                 pokecard5['height'],
                                                                                 pokecard5['weight'],
                                                                                 pokecard5['base_xp']))
        ## In case player inputs any number outside of 1 2 3 this code will propmt player to re-run the whole code
    else:
        return print('Battle Master: "You need to choose a pokemon! You cant go into battle without one!"')

cardforgame3()

print('\nYou chose to play {}'.format(cardforgame3()))

my_stat3 = input(
    '\nWhich stat would you like to play against {}? Choose between *id, height, weight, base xp*\n'.format(l))

def my_card_and_my_stat3():
    if chosen_card3 == 1:
        if my_stat3 == 'id':
            return pokecard1['id']
    if chosen_card3 == 1:
        if my_stat3 == 'height':
            return pokecard1['height']
    if chosen_card3 == 1:
        if my_stat3 == 'weight':
            return pokecard1['weight']
    if chosen_card3 == 1:
        if my_stat3 == 'base xp':
            return pokecard1['base_xp']
    if chosen_card3 == 2:
        if my_stat3 == 'id':
            return pokecard2['id']
    if chosen_card3 == 2:
        if my_stat3 == 'height':
            return pokecard2['height']
    if chosen_card3 == 2:
        if my_stat3 == 'weight':
            return pokecard2['weight']
    if chosen_card3 == 2:
        if my_stat3 == 'base xp':
            return pokecard2['base_xp']
    if chosen_card3 == 3:
        if my_stat3 == 'id':
            return pokecard3['id']
    if chosen_card3 == 3:
        if my_stat3 == 'height':
            return pokecard3['height']
    if chosen_card3 == 3:
        if my_stat3 == 'weight':
            return pokecard3['weight']
    if chosen_card3 == 3:
        if my_stat3 == 'base xp':
            return pokecard3['base_xp']
    if chosen_card3 == 4:
        if my_stat3 == 'id':
            return pokecard4['id']
    if chosen_card3 == 4:
        if my_stat3 == 'height':
            return pokecard4['height']
    if chosen_card3 == 4:
        if my_stat3 == 'weight':
            return pokecard4['weight']
    if chosen_card3 == 4:
        if my_stat3 == 'base xp':
            return pokecard4['base_xp']
    if chosen_card3 == 5:
        if my_stat3 == 'id':
            return pokecard5['id']
    if chosen_card3 == 5:
        if my_stat3 == 'height':
            return pokecard5['height']
    if chosen_card3 == 5:
        if my_stat3 == 'weight':
            return pokecard5['weight']
    if chosen_card3 == 5:
        if my_stat3 == 'base xp':
            return pokecard5['base_xp']
    else:
        return print('Battle Master: "You need to choose a stat from your chosen pokemon!"')

opponentscard()

def opponents_card_and_stat3():
    k = random.randint(1, 6)
    if k == 1:
        if my_stat3 == 'id':
            return oppcard1['id']
    if k == 1:
        if my_stat3 == 'height':
            return oppcard1['height']
    if k == 1:
        if my_stat3 == 'weight':
            return oppcard1['weight']
    if k == 1:
        if my_stat3 == 'base xp':
            return oppcard1['base_xp']

    if k == 2:
        if my_stat3 == 'id':
            return oppcard2['id']
    if k == 2:
        if my_stat3 == 'height':
            return oppcard2['height']
    if k == 2:
        if my_stat3 == 'weight':
            return oppcard2['weight']
    if k == 2:
        if my_stat3 == 'base xp':
            return oppcard2['base_xp']

    if k == 3:
        if my_stat3 == 'id':
            return oppcard3['id']
    if k == 3:
        if my_stat3 == 'height':
            return oppcard3['height']
    if k == 3:
        if my_stat3 == 'weight':
            return oppcard3['weight']
    if k == 3:
        if my_stat3 == 'base xp':
            return oppcard3['base_xp']

    if k == 4:
        if my_stat3 == 'id':
            return oppcard4['id']
    if k == 4:
        if my_stat3 == 'height':
            return oppcard4['height']
    if k == 4:
        if my_stat3 == 'weight':
            return oppcard4['weight']
    if k == 4:
        if my_stat3 == 'base xp':
            return oppcard4['base_xp']

    if k == 5:
        if my_stat3 == 'id':
            return oppcard5['id']
    if k == 5:
        if my_stat3 == 'height':
            return oppcard5['height']
    if k == 5:
        if my_stat3 == 'weight':
            return oppcard5['weight']
    if k == 5:
        if my_stat3 == 'base xp':
            return oppcard5['base_xp']

opponents_card_and_stat3()

print('Round 3! FIGHT!')

print('Results in 3... 2... 1...')

def results3():
    c = my_card_and_my_stat3()
    u = opponents_card_and_stat3()
    if c > u:
        with open('PokeScores.txt', 'a') as myfile:
            myfile.write('Player ' + str(3))
        print(
            '\nBattle Master: "Alright! {} wins round 3!\nYour stat was {}, {}s stat was {}"\n{} says: "Nooo! I cant believe I lost to someone like you!"'.format(
                q, c, l, u, l))
    if c < u:
        with open('PokeScores.txt', 'a') as myfile:
            myfile.write('Opponent 3' + str(3))
        print(
            '\nBattle Master: "You lose! {} wins round 3!\nYour stat was {}, {}s stat was {}"\n{} says "YES!! I knew id beat you!"'.format(
                l, c, l, u, l))
    elif c == u:
        print('\nBattle Master: "Aww! Its a draw"')

results3()

print('\nBattle Master: "{}s pokemons were {}, {}, {}, {}, {}"'.format(l, oppcard1['name'], oppcard2['name'], oppcard3['name'],
                                                           oppcard4['name'], oppcard5['name']))

def scoringquotes3():
    with open('PokeScores.txt') as myfile:
        for line in myfile:
            if 'Player ' + str(3) in line:
             print(
                '\nBattle Master: "After 3 intense rounds, we have a winner!\nAnd the battle arena champion is...\n{}!!!"\n{} says: "Good game {}... You beat me fair and square"'.format(
                    q, l, q))
            elif 'Opponent ' + str(3) in line:
                print(
                    '\nBattle Master: "After 3 intense rounds, the battle arena champion is {}!"\nBattle Master: "Keep training and dont give up {}, you have a bright future ahead of you"'.format(
                    l, q))
scoringquotes3()