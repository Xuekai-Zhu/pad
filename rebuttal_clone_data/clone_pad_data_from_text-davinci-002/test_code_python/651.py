def solution():
     hourly_wage = 9
     hours_worked_Monday = 4
     hours_worked_Wednesday = 3
     hours_worked_Friday = 6
     total_hours = hours_worked_Monday + hours_worked_Wednesday + hours_worked_Friday
     total_money_made = hourly_wage * total_hours
     result = total_money_made
     return result

print(solution())