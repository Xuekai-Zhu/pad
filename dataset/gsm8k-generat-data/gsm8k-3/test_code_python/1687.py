def solution():
    """A farmer hires small trucks to transport his lemons to the markets. The load on a truck may not be more than 900 kilograms. One bag of lemons has a mass of 8 kilograms. If there are 100 bags of lemons, how many more kilograms can still be loaded into the truck?"""
    # Define the maximum load capacity of the truck
    MAX_LOAD = 900

    # Define the weight of one bag of lemons
    BAG_WEIGHT = 8

    # Calculate the total weight of the lemons
    total_weight = BAG_WEIGHT * 100

    # Calculate the remaining weight that can be loaded onto the truck
    remaining_weight = MAX_LOAD - total_weight

    # Display the remaining weight
    result = remaining_weight
    return result

print(solution())