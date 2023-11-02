def solution():
    """Gail has two fish tanks. The first tank is twice the size of the second tank. There are 48 gallons of water in the first tank. She follows the rule of one gallon of water per inch of fish. If she keeps two-inch fish in the second tank and three-inch fish in the first tank, how many more fish would Gail have in the first tank than the second tank if one of the first tank fish eats another?"""
    second_tank_size = 48/2
    second_tank_fish = second_tank_size / 2
    first_tank_fish = 48 / 3 - 1
    difference = first_tank_fish - second_tank_fish
    result = difference
    return result

print(solution())