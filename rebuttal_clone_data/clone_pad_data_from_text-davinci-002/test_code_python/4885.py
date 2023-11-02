def solution():
    income_per_month = 1600
    living_expenses = income_per_month * 0.75
    insurance = income_per_month * 0.2
    savings = income_per_month - living_expenses - insurance
    result = savings
    return result

print(solution())