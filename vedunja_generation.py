import random

generation = [
    "третьем",
    "пятом",
    "седьмом",
    "осьмом",
    "девятом",
    "пятнадцатом",
    "двадцатом",
    "полсотнитретьем",
    "стотрёхсотом"]

def get_random_generation():
    return random.choice(generation)
