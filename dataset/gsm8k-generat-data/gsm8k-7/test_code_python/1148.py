def solution():
    grains_per_cup = 480
    half_cup_in_tablespoons = 8
    tablespoons_per_teaspoon = 3

    # Calculate the total number of grains in half a cup
    grains_in_half_cup = grains_per_cup / 2

    # Calculate the total number of teaspoons in half a cup
    teaspoons_in_half_cup = half_cup_in_tablespoons / tablespoons_per_teaspoon

    # Calculate the number of grains of rice in a teaspoon
    grains_per_teaspoon = grains_in_half_cup / teaspoons_in_half_cup
    result = grains_per_teaspoon
    return result

print(solution())