def solution():
    savings = [27, 13, 28]
    expenses = [49, 5]

    total_savings = sum(savings)
    total_expenses = sum(expenses)

    money_left = total_savings - total_expenses
    result = money_left
    return result

print(solution())