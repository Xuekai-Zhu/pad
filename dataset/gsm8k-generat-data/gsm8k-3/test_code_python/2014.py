def solution():
    """Jennifer is building tanks to hold her goldfish. She built 3 tanks that will hold 15 fish each, heated, and filled them. She plans to build the rest of the tanks equipped with heaters, and they will hold 10 fish each. If she needs to build enough tanks to house a total of 75 fish, how many more will she need to build?"""
    # Define the number of fish that can be held in each tank
    HEATED_TANK_CAPACITY = 15
    UNHEATED_TANK_CAPACITY = 10

    # Define the number of heated tanks Jennifer has already built
    num_heated_tanks = 3
    heated_tank_capacity = num_heated_tanks * HEATED_TANK_CAPACITY

    # Calculate the number of fish that can be held in the remaining tanks
    remaining_tank_capacity = 75 - heated_tank_capacity

    # Calculate the number of unheated tanks needed to hold the remaining fish
    num_unheated_tanks = remaining_tank_capacity // UNHEATED_TANK_CAPACITY

    # Check if there's a remainder and add one more tank if needed
    if remaining_tank_capacity % UNHEATED_TANK_CAPACITY != 0:
        num_unheated_tanks += 1

    # Display the total number of tanks needed
    result = num_heated_tanks + num_unheated_tanks - 3  # subtracting initial 3 because they were already built
    return result

print(solution())