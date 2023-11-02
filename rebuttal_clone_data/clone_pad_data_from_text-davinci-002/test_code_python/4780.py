def solution():
     hour_wage = 10
     hours_worked = 35
     days_worked = 5
     hours_worked_2 = 40
     wage_increase = 0.50
     new_hour_wage = hour_wage + wage_increase
     total_hours = hours_worked + hours_worked_2
     total_wage = (hour_wage * hours_worked) + (new_hour_wage * hours_worked_2)
     result = total_wage
     return result

print(solution())