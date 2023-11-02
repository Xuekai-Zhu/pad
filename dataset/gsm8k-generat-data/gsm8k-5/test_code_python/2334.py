def solution():
    # Calculate the number of fish in the first tank
    first_tank_fishes = 7 + 8  # First tank has 7 goldfish and 8 beta fish

    # Calculate the number of fish in the second tank
    second_tank_fishes = 2 * first_tank_fishes  # Second tank has double the number of fish in the first tank

    # Calculate the number of fish in the third tank
    third_tank_fishes = second_tank_fishes // 3  # Third tank has a third of the number of fish in the second tank

    result = third_tank_fishes
    return result

print(solution())