def solution():
    """Gail has two fish tanks. The first tank is twice the size of the second tank. There are 48 gallons of water in the first tank. She follows the rule of one gallon of water per inch of fish. If she keeps two-inch fish in the second tank and three-inch fish in the first tank, how many more fish would Gail have in the first tank than the second tank if one of the first tank fish eats another?"""
    # Define the size ratios of the two tanks
    size_ratio = 2

    # Calculate the size of the second tank
    second_tank_size = 48 / size_ratio

    # Calculate the number of fish in the second tank
    second_tank_fish = second_tank_size / 2

    # Calculate the number of fish in the first tank
    first_tank_fish = (48 / 3) - 1

    # Calculate the difference in fish between the two tanks
    fish_difference = first_tank_fish - second_tank_fish

    # Return the result
    result = fish_difference
    return result

print(solution())