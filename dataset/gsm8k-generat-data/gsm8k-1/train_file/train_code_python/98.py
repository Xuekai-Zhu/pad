def solution():
    """Gail has two fish tanks. The first tank is twice the size of the second tank. There are 48 gallons of water in the first tank.
    She follows the rule of one gallon of water per inch of fish. If she keeps two-inch fish in the second tank and three-inch fish in the first tank,
    how many more fish would Gail have in the first tank than the second tank if one of the first tank fish eats another?"""
    second_tank_size = 48 / 2  # 24 gallons
    second_tank_fish = second_tank_size / 1  # one inch of fish per gallon of water
    first_tank_fish = 48 / 3  # three inches of fish per gallon of water
    difference = first_tank_fish - (second_tank_fish - 1) # subtract one fish eaten from first tank
    result = difference
    return result

print(solution())