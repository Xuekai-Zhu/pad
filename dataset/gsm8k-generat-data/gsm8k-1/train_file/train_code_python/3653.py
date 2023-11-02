def solution():
    """Philip has a farm with animals. He has 20 cows, 50% more ducks. Philip also has as many pigs as one-fifth of ducks and cows in total. How many animals does Philip have on his farm?"""
    cows = 20
    ducks = cows * 1.5
    total_animals = cows + ducks + (cows + ducks) / 5
    result = total_animals
    return result

print(solution())