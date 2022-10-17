import random

# Initial wordlists
fours = []
fives = []
sixes = []
sevens = []

# Fill above lists with corresponding word lengths from wordlist
with open('wordlist.txt') as wordlist:
    for line in wordlist:
        if len(line) == 4:
            fours.append(line.strip())
        elif len(line) == 5:
            fives.append(line.strip())
        elif len(line) == 6:
            sixes.append(line.strip())
        elif len(line) == 7:
            sevens.append(line.strip())

# Create new lists and fill with number of items in fours
fivesLess = []
sixesLess = []
sevensLess = []

fivesCounter = 0
while fivesCounter < len(fours):
    randFive = random.choice(fives)
    if randFive not in fivesLess:
        fivesLess.append(randFive)
        fivesCounter += 1

sixesCounter = 0
while sixesCounter < len(fours):
    randSix = random.choice(sixes)
    if randSix not in sixesLess:
        sixesLess.append(randSix)
        sixesCounter += 1

sevensCounter = 0
while sevensCounter < len(fours):
    randSeven = random.choice(sevens)
    if randSeven not in sevensLess:
        sevensLess.append(randSeven)
        sevensCounter += 1

choices = [fours, fivesLess, sixesLess, sevensLess]

# Generate n number of seeds and print
seedCounter = 0
while seedCounter < 1:
    seed = []
    while len(seed) < 12:
        wordLengthChoice = random.choice(choices)
        wordChoice = random.choice(wordLengthChoice)
        seed.append(wordChoice)
    seedCounter += 1

    print(' '.join(seed))