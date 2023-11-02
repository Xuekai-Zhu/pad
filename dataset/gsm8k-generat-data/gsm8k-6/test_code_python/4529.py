def solution():
    # Calculate the total cost for building one floor of a house by one builder
    cost_one_floor_one_builder = 100 * 30  # each builder is paid $100 for a single day's work for 30 days

    # Calculate the total cost for building one house with 6 floors by 3 builders
    cost_one_house_6_floors_3_builders = cost_one_floor_one_builder * 6 * 3  # three builders build a single floor of a house in 30 days

    # Calculate the total cost for building 5 houses with 6 floors each by 6 builders
    total_cost = cost_one_house_6_floors_3_builders * 5 / 3 * 6  # six builders build 3 floors of a house in 30 days, so 6 builders can build 6 floors in 60 days
    result = total_cost
    return result

print(solution())