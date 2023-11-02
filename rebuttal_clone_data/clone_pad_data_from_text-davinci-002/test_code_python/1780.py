def solution():
     hourly_rate = 13.50
     hours_worked = 8
     days_worked = 5
     overtime = 2
     regular_pay = hours_worked * hourly_rate
     overtime_pay = (hours_worked + overtime) * (hourly_rate * 1.5)
     total_pay = regular_pay + (overtime_pay * days_worked)
     result = total_pay
     return result

print(solution())