def solution():
     hours_worked = 40
     current_rate = 30
     freelance_rate = 40
     fica_taxes = 25
     healthcare_premiums = 400
     weeks_in_month = 4
     monthly_hours = hours_worked * weeks_in_month
     current_pay = monthly_hours * current_rate
     freelance_pay = monthly_hours * freelance_rate
     freelance_net_pay = freelance_pay - fica_taxes - healthcare_premiums
     monthly_difference = freelance_net_pay - current_pay
 
     return monthly_difference

print(solution())