def solution():
    # Define the cost per day and the number of days for each book
    cost_per_day = 0.5
    days_1 = 20
    days_2 = 31
    days_3 = 31

    # Calculate the total cost for each book
    cost_1 = days_1 * cost_per_day
    cost_2 = days_2 * cost_per_day
    cost_3 = days_3 * cost_per_day

    # Calculate the total cost for all three books
    total_cost = cost_1 + cost_2 + cost_3
    result = total_cost
    return result

print(solution())