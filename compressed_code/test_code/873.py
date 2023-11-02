def solution():
    
    grains_per_cup = 480
    tablespoons_per_half_cup = 8
    teaspoons_per_tablespoon = 3

    grains_per_half_cup = grains_per_cup / 2
    grains_per_tablespoon = grains_per_half_cup / tablespoons_per_half_cup
    grains_per_teaspoon = grains_per_tablespoon / teaspoons_per_tablespoon

    result = grains_per_teaspoon
    return result

print(solution())