def solution():
    total_profit = 1200

    # Calculate the profit earned on Monday
    monday_profit = total_profit / 3

    # Calculate the profit earned on Tuesday
    tuesday_profit = total_profit / 4

    # Calculate the profit earned on Wednesday
    wednesday_profit = total_profit - monday_profit - tuesday_profit
    result = wednesday_profit
    return result

print(solution())