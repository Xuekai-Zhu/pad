def solution():
    total_cost = 4 * 1863  # The developer spent $1,863 per acre to buy 4 acres of land
    number_of_lots = 9  # The developer split the land into 9 lots

    # Calculate the cost per lot
    cost_per_lot = total_cost / number_of_lots

    result = cost_per_lot
    return result

print(solution())