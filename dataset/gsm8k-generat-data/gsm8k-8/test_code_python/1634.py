def solution():
    # Calculate the cost per cup of lemonade
    cost_per_cup = 20 / x

    # Calculate the profit per cup of lemonade
    profit_per_cup = 2 - cost_per_cup

    # Calculate the number of cups of lemonade needed to make a profit of $80
    cups_needed = 80 / profit_per_cup
    result = cups_needed
    return result

print(solution())