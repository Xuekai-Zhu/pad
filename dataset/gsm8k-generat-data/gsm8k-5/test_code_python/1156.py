def solution():
    total_profit = 1200  # Total profit made by the shop
    monday_profit = total_profit / 3  # Profit made on Monday is one third of the total profit
    tuesday_profit = total_profit / 4  # Profit made on Tuesday is one quarter of the total profit
    wednesday_profit = total_profit - monday_profit - tuesday_profit  # Profit made on Wednesday is the remaining profit

    result = wednesday_profit
    return result

print(solution())