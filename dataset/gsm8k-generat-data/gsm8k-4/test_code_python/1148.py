def solution():
    """There are 480 grains of rice in one cup. If half a cup is 8 tablespoons and one tablespoon is 3 teaspoons, how many grains of rice are in a teaspoon?"""
    # Define the number of grains of rice in one cup
    grains_in_cup = 480

    # Calculate the number of grains of rice in half a cup, which is 8 tablespoons
    grains_in_half_cup = grains_in_cup / 2
    grains_in_tablespoon = grains_in_half_cup / 8

    # Calculate the number of grains of rice in one teaspoon
    grains_in_teaspoon = grains_in_tablespoon / 3

    result = grains_in_teaspoon
    return result

print(solution())