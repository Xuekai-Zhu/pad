def solution():
    """Adam had a farm with animals. He had 12 cows and twice as many sheep. He decided to buy 3 pigs for every sheep he had. How many animals were on the farm after the transaction?"""
    cows = 12
    sheep = 2 * cows
    pigs = 3 * sheep
    total_animals = cows + sheep + pigs
    result = total_animals
    return result

print(solution())