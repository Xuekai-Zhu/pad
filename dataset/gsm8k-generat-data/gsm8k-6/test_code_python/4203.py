def solution():
    # Calculate Kyle's total monthly expenses
    total_expenses = 1250 + 150 + 400 + 300 + 200 + 200 + 350  # rent, utilities, retirement/savings, groceries/eating out, insurance, miscellaneous, car payment
    monthly_income = 3200  # Kyle's monthly income
    remaining_income = monthly_income - total_expenses  # Kyle's remaining income after deducting expenses
    result = remaining_income
    return result

print(solution())