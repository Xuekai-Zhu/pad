def solution():
    """There are 480 grains of rice in one cup. If half a cup is 8 tablespoons and one tablespoon is 3 teaspoons, how many grains of rice are in a teaspoon?"""
    # Define the number of grains of rice in one cup
    RICE_IN_CUP = 480

    # Calculate the number of grains of rice in half a cup
    rice_in_half_cup = RICE_IN_CUP / 2

    # Calculate the number of grains of rice in one tablespoon
    rice_in_tablespoon = rice_in_half_cup / 8

    # Calculate the number of grains of rice in one teaspoon
    rice_in_teaspoon = rice_in_tablespoon / 3

    # Display the number of grains of rice in one teaspoon
    result = rice_in_teaspoon
    return result

print(solution())