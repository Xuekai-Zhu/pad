def solution():
    """A farmer hires small trucks to transport his lemons to the markets. The load on a truck may not be more than 900 kilograms. One bag of lemons has a mass of 8 kilograms. If there are 100 bags of lemons, how many more kilograms can still be loaded into the truck?"""
    bag_weight = 8
    total_weight = bag_weight * 100
    remaining_weight = 900 - total_weight
    result = remaining_weight
    return result

print(solution())