def solution():
     daily_rate = 8
     days_worked = 5
     overtime_rate = 1.5
     overtime_days = 1
     regular_pay = daily_rate * days_worked
     overtime_pay = (daily_rate * overtime_rate) * overtime_days
     monthly_pay = regular_pay + overtime_pay
     result = monthly_pay
     return result

print(solution())