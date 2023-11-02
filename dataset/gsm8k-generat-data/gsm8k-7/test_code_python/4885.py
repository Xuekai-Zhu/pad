def solution():
    monthly_income = 1600
    living_expenses = monthly_income * 0.75
    insurance = monthly_income * 0.2

    # Calculate the amount of money Jade saves per month
    savings = monthly_income - living_expenses - insurance
    result = savings
    return result

print(solution())