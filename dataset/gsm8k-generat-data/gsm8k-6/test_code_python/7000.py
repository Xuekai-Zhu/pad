def solution():
    # Calculate the cost and revenue of buying and selling candy bars
    cost = 50 * 0.8  # Jen buys 50 candy bars for 80 cents each
    revenue = 48 * 1  # Jen sells 48 candy bars for a dollar each

    # Calculate the profit Jen makes in cents
    profit = (revenue - cost) * 100  # profit = (revenue - cost) * 100 cents / dollar
    result = profit
    return result

print(solution())