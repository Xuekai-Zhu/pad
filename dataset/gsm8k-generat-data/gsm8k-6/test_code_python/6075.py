def solution():
    # Calculate the total cost of hiring two bodyguards for 8 hours per day
    cost_per_day = 2 * 20 * 8  # two bodyguards charge $20 an hour for 8 hours
    total_cost_per_week = cost_per_day * 7  # hired for 7 days in a week
    result = total_cost_per_week
    return result

print(solution())