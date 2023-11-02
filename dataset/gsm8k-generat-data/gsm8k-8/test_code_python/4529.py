def solution():
    # Calculate the cost to build one floor of one house with three builders
    cost_per_floor = 100 * 3 * 30

    # Calculate the total cost to build one house with six floors
    total_cost_per_house = cost_per_floor * 6

    # Calculate the total cost to build five houses with six floors each
    total_cost = total_cost_per_house * 5

    # Calculate the cost to hire six builders to do the work
    cost_with_six_builders = total_cost / (6 * 30)

    result = cost_with_six_builders
    return result

print(solution())