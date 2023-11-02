def solution():
    # Calculate the amount of gas used per day
    gas_per_day = 75 / 50

    # Calculate the cost of gas per day
    cost_per_day = gas_per_day * 3

    # Calculate the total cost of gas for 10 days
    total_cost = cost_per_day * 10
    result = total_cost
    return result

print(solution())