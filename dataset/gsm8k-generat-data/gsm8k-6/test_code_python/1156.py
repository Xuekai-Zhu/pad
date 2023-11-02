def solution():
    # Calculate the profit made on Wednesday
    monday_profit = 1200 / 3  # a third of the total profit
    tuesday_profit = 1200 / 4  # a quarter of the total profit
    wednesday_profit = 1200 - monday_profit - tuesday_profit  # the remaining profit
    result = wednesday_profit
    return result

print(solution())