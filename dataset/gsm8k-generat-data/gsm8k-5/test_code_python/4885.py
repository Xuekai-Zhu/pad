def solution():
    monthly_income = 1600  # Jade earns $1600 per month
    living_expenses = monthly_income * 0.75  # 75% of her income goes to living expenses
    insurance = monthly_income * (1/5)  # One-fifth of her income goes to insurance
    saved_amount = monthly_income - living_expenses - insurance  # The rest of her income goes to savings

    result = saved_amount
    return result

print(solution())