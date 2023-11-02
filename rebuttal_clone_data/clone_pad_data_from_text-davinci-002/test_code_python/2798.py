def solution():
     hours_worked = 12
     days_worked = 15
     hourly_wage = 20
     percent_raise = 30
     hourly_raise = (hourly_wage * (percent_raise/100))
     new_hourly_wage = hourly_wage + hourly_raise
     total_hours = hours_worked * days_worked
     total_pay = new_hourly_wage * total_hours
     result = total_pay
     
     return result

print(solution())