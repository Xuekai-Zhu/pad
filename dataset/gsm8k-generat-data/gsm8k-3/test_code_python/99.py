def solution():
    """Gail has two fish tanks. The first tank is twice the size of the second tank. There are 48 gallons of water in the first tank. She follows the rule of one gallon of water per inch of fish. If she keeps two-inch fish in the second tank and three-inch fish in the first tank, how many more fish would Gail have in the first tank than the second tank if one of the first tank fish eats another?"""
    # Define the size of the second tank in gallons
    second_tank_size = 48/2

    # Calculate the number of two-inch fish that can fit in the second tank
    second_tank_fish = second_tank_size

    # Calculate the number of three-inch fish that can fit in the first tank
    first_tank_fish = 48 - 3*(second_tank_fish)

    # Remove one fish from the first tank
    first_tank_fish -= 1

    # Calculate the difference in the number of fish between the two tanks
    fish_difference = first_tank_fish - second_tank_fish

    # Return the result
    result = fish_difference
    return result

print(solution())