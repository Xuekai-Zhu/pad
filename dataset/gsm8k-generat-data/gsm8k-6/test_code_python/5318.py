def solution():
    # Calculate the cost of staying for 3 months by paying weekly
    weekly_cost = 280 * 12  # 3 months, each with 4 weeks
    # Calculate the cost of staying for 3 months by paying monthly
    monthly_cost = 1000 * 3
    # Calculate the amount saved by paying monthly
    saved_money = weekly_cost - monthly_cost
    result = saved_money
    return result

print(solution())