def solution():
    # Calculate the total number of grains of rice in half a cup
    rice_in_half_cup = 480 * 0.5

    # Calculate the number of grains of rice in one tablespoon
    rice_in_one_tablespoon = rice_in_half_cup / 8

    # Calculate the number of grains of rice in one teaspoon
    rice_in_one_teaspoon = rice_in_one_tablespoon / 3

    result = rice_in_one_teaspoon
    return result

print(solution())