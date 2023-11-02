def solution():
    """Adam had a farm with animals. He had 12 cows and twice as many sheep. He decided to buy 3 pigs for every sheep he had. How many animals were on the farm after the transaction?"""
    cows = 12
    sheep = cows * 2
    pigs_per_sheep = 3
    pigs = sheep * pigs_per_sheep
    total_animals = cows + sheep + pigs
    result = total_animals
    return result

print(solution())