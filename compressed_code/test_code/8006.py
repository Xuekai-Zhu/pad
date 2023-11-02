def solution():
    
    hours_per_workday = 12
    workdays_per_month = 15
    former_rate = 20
    raise_percent = 30
    new_rate = former_rate * (1 + (raise_percent / 100))
    total_income = new_rate * hours_per_workday * workdays_per_month
    result = total_income
    return result

print(solution())