def solution():
    """Jennifer is building tanks to hold her goldfish. She built 3 tanks that will hold 15 fish each, heated, and filled them. She plans to build the rest of the tanks equipped with heaters, and they will hold 10 fish each. If she needs to build enough tanks to house a total of 75 fish, how many more will she need to build?"""
    heated_tanks = 3
    heated_tank_capacity = 15
    remaining_fish = 75 - (heated_tanks * heated_tank_capacity)
    additional_tanks_capacity = 10
    additional_tanks_needed = remaining_fish // additional_tanks_capacity
    if remaining_fish % additional_tanks_capacity != 0:
        additional_tanks_needed += 1

    result = additional_tanks_needed
    return result

print(solution())