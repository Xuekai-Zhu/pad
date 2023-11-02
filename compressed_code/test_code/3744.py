def solution():
    
    visits_per_hour = 50
    hours_per_day = 24
    days_per_month = 30
    visit_pay = 0.10
    total_visits = visits_per_hour * hours_per_day * days_per_month
    total_income = total_visits * visit_pay
    result = total_income
    return result

print(solution())