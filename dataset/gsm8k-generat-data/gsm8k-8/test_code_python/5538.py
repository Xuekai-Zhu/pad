def solution():
    # Define the ratio of cows to bulls
    cow_to_bull_ratio = 10/27

    # Calculate the total number of cattle
    total_cattle = 555

    # Calculate the total number of units in the ratio
    total_units = 10 + 27

    # Calculate the value of one unit
    one_unit = total_cattle / total_units

    # Calculate the number of bulls on the farm
    bulls = 27 * one_unit
    result = bulls
    return result

print(solution())