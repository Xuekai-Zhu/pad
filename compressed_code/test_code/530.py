def solution():
    
    monthly_visits = 30000
    visit_pay = 0.01
    total_income = monthly_visits * visit_pay
    daily_income = total_income / 30
    result = daily_income
    return result

print(solution())