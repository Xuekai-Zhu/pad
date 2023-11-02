def solution():
    total_savings = 0
    remaining_savings = 2900

    # Calculate how much was left in Reese's savings account after April expenses
    remaining_savings += 1500

    # Calculate how much Reese spent in March
    march_expenses = remaining_savings / 0.4
    remaining_savings += march_expenses

    # Calculate how much Reese spent in February
    feb_expenses = remaining_savings / 0.2
    remaining_savings += feb_expenses

    total_savings = remaining_savings
    result = total_savings
    return result

print(solution())