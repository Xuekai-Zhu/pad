def solution():
    # Calculate the total cost of yarn for 28 sweaters
    cost_of_yarn = 4 * 6 * 28  # 4 balls of yarn cost $6 each for each sweater, and there are 28 sweaters
    total_revenue = 35 * 28  # Chantal sells each sweater for $35 and sells 28 sweaters

    # Calculate the total profit
    total_profit = total_revenue - cost_of_yarn
    result = total_profit
    return result

print(solution())