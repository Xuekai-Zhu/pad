def solution():
    # Calculate the cost and revenue of selling 5 boxes of candy bars
    cost = 5 * 10 * 1  # 5 boxes with 10 candy bars in each box at $1 each
    revenue = 5 * 10 * 1.5  # 5 boxes with 10 candy bars in each box at $1.50 each

    # Calculate the profit from these sales
    profit = revenue - cost
    result = profit
    return result

print(solution())