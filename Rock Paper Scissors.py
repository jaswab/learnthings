import random
i = 1
while i == 1:
    #Player 2 decides rock, paper, or scissors at random
    inputplayer1 = input('Please enter Rock, Paper, or Scissors\n').lower()

    #Player 2 decides rock, paper, or scissors at random

    #Playing the game
    #1 = rock
    #2 = paper
    #3 = scissors


    if inputplayer1 == 'rock':
        inputplayer2 = random.choice(['rock', 'paper', 'scissors'])
        if inputplayer2 == 'rock':
            print('Player has chosen ' + inputplayer2)
            print('Tie! Play again?')
            i = int(input('Enter 0 to quit and 1 to continue\n'))

        if inputplayer2 == 'paper':
            print('Player has chosen ' + inputplayer2)
            print('You Lose! Play again?')
            i = int(input('Enter 0 to quit and 1 to continue\n'))
        if inputplayer2 == 'scissors':
            print('Player has chosen ' + inputplayer2)
            print('You win! Play again?')
            i = int(input('Enter 0 to quit and 1 to continue\n'))

    if inputplayer1 == 'paper':
        inputplayer2 = random.choice(['rock', 'paper', 'scissors'])
        if inputplayer2 == 'rock':
            print('Player has chosen ' + inputplayer2)
            print('You Win! Play again?')
            i = int(input('Enter 0 to quit and 1 to continue\n'))
        if inputplayer2 == 'paper':
            print('Player has chosen ' + inputplayer2)
            print('Tie! Play again?')
        if inputplayer2 == 'scissors':
            print('Player has chosen ' + inputplayer2)
            print('You Lose! Play again?')
            i = int(input('Enter 0 to quit and 1 to continue\n'))

    if inputplayer1 == 'scissors':
        inputplayer2 = random.choice(['rock', 'paper', 'scissors'])
        if inputplayer2 == 'rock':
            print('Player has chosen ' + inputplayer2)
            print('You Lose! Play again?')
            i = int(input('Enter 0 to quit and 1 to continue\n'))
        if inputplayer2 == 'paper':
            print('Player has chosen ' + inputplayer2)
            print('You Win! Play again?')
            i = int(input('Enter 0 to quit and 1 to continue\n'))
        if inputplayer2 == 'scissors':
            print('Player has chosen ' + inputplayer2)
            print('Tie! Play again?')
            i = int(input('Enter 0 to quit and 1 to continue\n'))

print('Thanks for playing!')