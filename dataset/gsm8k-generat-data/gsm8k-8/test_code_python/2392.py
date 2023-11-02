def solution():
    # Calculate the revenue from selling 60 computers
    selling_price = 1.4 * 800
    revenue = selling_price * 60

    # Calculate the total expenses
    total_expenses = 5000 + 3000 + 800 * 60

    # Calculate the profit
    profit = revenue - total_expenses
    result = profit
    return result

print(solution())