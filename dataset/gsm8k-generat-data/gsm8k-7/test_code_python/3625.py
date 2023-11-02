def solution():
    cost_per_pound = 7
    num_pounds = 2
    payment = 20

    # Calculate the total cost of the steak
    total_cost = cost_per_pound * num_pounds

    # Calculate the amount of change Ken will receive
    change = payment - total_cost
    result = change
    return result

print(solution())