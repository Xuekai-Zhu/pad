def solution():
    """A farmer hires small trucks to transport his lemons to the markets. The load on a truck may not be more than 900 kilograms. One bag of lemons has a mass of 8 kilograms. If there are 100 bags of lemons, how many more kilograms can still be loaded into the truck?"""
    max_load = 900  # maximum load of the truck in kilograms
    lemon_bag_weight = 8  # weight of one bag of lemons in kilograms
    num_bags = 100  # number of bags of lemons
    total_weight = num_bags * lemon_bag_weight  # total weight of the lemons in kilograms
    remaining_capacity = max_load - total_weight  # remaining capacity of the truck in kilograms
    result = remaining_capacity
    return result

print(solution())