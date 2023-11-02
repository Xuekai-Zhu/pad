def solution():
    grains_per_cup = 480  # There are 480 grains of rice in one cup
    half_cup = 8  # Half a cup is 8 tablespoons
    tablespoons_per_cup = 16  # There are 16 tablespoons in one cup
    teaspoons_per_tablespoon = 3  # There are 3 teaspoons in one tablespoon

    # Calculate the number of grains of rice in half a cup
    grains_half_cup = grains_per_cup / 2

    # Calculate the number of grains of rice in one tablespoon
    grains_per_tablespoon = grains_half_cup / half_cup

    # Calculate the number of grains of rice in one teaspoon
    grains_per_teaspoon = grains_per_tablespoon / teaspoons_per_tablespoon
    result = grains_per_teaspoon
    return result

print(solution())