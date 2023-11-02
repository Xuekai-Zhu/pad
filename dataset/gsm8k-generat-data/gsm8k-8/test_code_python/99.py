def solution():
    # Calculate the size of the second tank
    second_tank_size = 48 / 2

    # Calculate the number of fish in the second tank
    second_tank_fish_count = second_tank_size / 2

    # Calculate the size of the first tank
    first_tank_size = 48

    # Calculate the number of fish in the first tank
    first_tank_fish_count = first_tank_size / 3

    # Subtract the number of fish in the second tank from the number of fish in the first tank
    fish_difference = first_tank_fish_count - second_tank_fish_count - 1

    result = fish_difference
    return result

print(solution())