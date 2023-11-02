def solution():
    """Three builders build a single floor of a house in 30 days. If each builder is paid $100 for a single day’s work, how much would it cost to hire 6 builders to build 5 houses with 6 floors each?"""
    
    # Define the number of builders and the time it takes to build a floor
    num_builders = 3
    time_per_floor = 30

    # Define the cost per builder per day
    cost_per_builder_per_day = 100

    # Calculate the time it takes to build one house
    time_per_house = 6 * time_per_floor

    # Calculate the cost of building one house with three builders
    cost_per_house = num_builders * time_per_house * cost_per_builder_per_day

    # Calculate the cost of building 5 houses with six floors each
    total_cost = 5 * 6 * cost_per_house

    # return the result
    result = total_cost
    return result

print(solution())