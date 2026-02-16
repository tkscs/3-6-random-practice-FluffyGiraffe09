import random
suits = "♠♥♣♦"
values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck = []
for x in range (13):
    spade = suits[0]+ values[x]
    heart = suits[1] + values[x]
    club = suits[2] + values[x]
    diomand = suits[3] + values[x]
    deck = deck + [spade, heart, club, diomand]
print(deck)
random.shuffle(deck)
print(deck)
print(random.sample(deck, k = 5))
