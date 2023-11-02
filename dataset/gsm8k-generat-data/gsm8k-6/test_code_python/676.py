def solution():
    # Calculate the cost of one pill after insurance coverage
    cost_per_pill = 1.5 * (1 - 0.4)  # the insurance covers 40% of the cost

    # Calculate the total cost of pills for 30 days
    total_cost = 2 * cost_per_pill * 30  # John needs to take 2 pills a day for 30 days

    result = total_cost
    return result

print(solution())