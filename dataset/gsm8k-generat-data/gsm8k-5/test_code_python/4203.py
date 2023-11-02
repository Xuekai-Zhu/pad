def solution():
    total_income = 3200.00  # Kyle makes $3200 every month
    total_expenses = 1250.00 + 150.00 + 400.00 + 300.00 + 200.00 + 200.00  # Kyle's total monthly expenses

    # Calculate Kyle's monthly disposable income after all the expenses
    disposable_income = total_income - total_expenses

    # Subtract the monthly car payment from disposable income to get the amount left for gas and maintenance
    amount_left = disposable_income - 350.00
    result = amount_left
    return result

print(solution())