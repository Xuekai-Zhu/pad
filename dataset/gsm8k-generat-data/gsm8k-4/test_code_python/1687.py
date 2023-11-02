def solution():
    """A farmer hires small trucks to transport his lemons to the markets. The load on a truck may not be more than 900 kilograms. One bag of lemons has a mass of 8 kilograms. If there are 100 bags of lemons, how many more kilograms can still be loaded into the truck?"""
    # Define the maximum load of the truck and the mass of one bag of lemons
    MAX_LOAD = 900
    BAG_MASS = 8

    # Calculate the total mass of 100 bags of lemons
    total_mass = 100 * BAG_MASS

    # Calculate the remaining load that can still be loaded into the truck
    remaining_load = MAX_LOAD - total_mass

    # return the result
    result = remaining_load
    return result

print(solution())