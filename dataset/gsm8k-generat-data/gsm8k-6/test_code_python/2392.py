def solution():
    # Calculate the revenue from selling 60 computers
    revenue = 1.4 * 800 * 60  # selling price is 1.4 times the cost of components, and he sells 60 computers

    # Calculate the total expenses
    expenses = 5000 + 3000  # $5000 in rent and $3000 in non-rent expenses

    # Calculate the profit
    profit = revenue - expenses

    result = profit
    return result

print(solution())