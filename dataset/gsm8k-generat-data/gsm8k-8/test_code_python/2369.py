def solution():
    # Calculate the cost for 14 days
    cost_14_days = 500

    # Calculate the cost per day
    cost_per_day = 50

    # Calculate the additional days Eric wants to rent
    additional_days = 20 - 14

    # Calculate the total cost for Eric's rental
    total_cost = cost_14_days + (additional_days * cost_per_day)
    result = total_cost
    return result

print(solution())