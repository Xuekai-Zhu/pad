def solution():
    """There are 480 grains of rice in one cup. If half a cup is 8 tablespoons and one tablespoon is 3 teaspoons, how many grains of rice are in a teaspoon?"""
    grains_per_cup = 480
    tablespoons_per_half_cup = 8
    teaspoons_per_tablespoon = 3
    grains_per_teaspoon = (grains_per_cup / 2) / (tablespoons_per_half_cup * teaspoons_per_tablespoon)
    result = grains_per_teaspoon
    return result

print(solution())