import random

with open("cows.txt") as f:
    cows = f.read().split("\n\n\n")

def random_cow():
    return random.choice(cows)
