def solution():
    # Calculate the total cost of the laundry bill
    total_cost = 140

    # Calculate the number of trousers dropped off
    num_trousers = 10

    # Calculate the cost of the trousers
    trouser_cost = num_trousers * 9

    # Calculate the remaining cost, which is the cost of the shirts
    remaining_cost = total_cost - trouser_cost

    # Calculate the number of shirts dropped off
    num_shirts = remaining_cost / 5

    # Calculate the number of missing shirts
    missing_shirts = 10 - num_shirts

    result = missing_shirts
    return result

print(solution())