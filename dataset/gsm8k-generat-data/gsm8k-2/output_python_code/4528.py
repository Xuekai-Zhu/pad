def solution():
    """Three builders build a single floor of a house in 30 days. If each builder is paid $100 for a single day’s work, how much would it cost to hire 6 builders to build 5 houses with 6 floors each?"""
    num_builders = 6
    num_houses = 5
    num_floors = 6

    # Calculate the time it takes one builder to build one floor
    single_builder_time = 30

    # Calculate the total cost for one builder to work for one day
    cost_per_builder = 100

    # Calculate the total time it takes to build all the floors
    total_floors = num_houses * num_floors
    total_time = total_floors * single_builder_time / num_builders

    # Calculate the total cost of hiring all the builders
    total_cost = num_builders * total_time * cost_per_builder

    result = total_cost
    return result

print(solution())