def solution():
    """Jennifer is building tanks to hold her goldfish. She built 3 tanks that will hold 15 fish each, heated, and filled them. She plans to build the rest of the tanks equipped with heaters, and they will hold 10 fish each. If she needs to build enough tanks to house a total of 75 fish, how many more will she need to build?"""
    # Define the number of tanks already built and the capacity of each tank
    tanks_built = 3
    tank_capacity_1 = 15

    # Calculate the total capacity of the tanks already built
    total_capacity_1 = tanks_built * tank_capacity_1

    # Define the capacity of the remaining tanks
    tank_capacity_2 = 10

    # Calculate the number of tanks needed to house the remaining fish
    remaining_fish = 75 - total_capacity_1
    tanks_needed = remaining_fish // tank_capacity_2

    result = tanks_needed
    return result

print(solution())