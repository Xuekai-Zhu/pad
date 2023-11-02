def solution():
    # Calculate the size of the second tank
    second_tank_size = 48 / 2  # The first tank is twice the size of the second tank

    # Calculate the total number of fish in each tank
    first_tank_fish = 48 / 3  # There is one three-inch fish per gallon in the first tank
    second_tank_fish = second_tank_size / 2  # There is one two-inch fish per gallon in the second tank

    # Subtract the number of fish in the second tank from the number of fish in the first tank
    difference = first_tank_fish - second_tank_fish - 1  # Subtract one because one fish eats another

    result = difference
    return result

print(solution())