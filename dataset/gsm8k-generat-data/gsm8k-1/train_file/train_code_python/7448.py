def solution():
    """Mr. Rainwater has some goats, 9 cows and some chickens. He has 4 times as many goats as cows and 2 times as many goats as chickens. How many chickens does he have?"""
    cows = 9
    goats = 4 * cows
    chickens = goats / 2
    result = chickens
    return result

print(solution())