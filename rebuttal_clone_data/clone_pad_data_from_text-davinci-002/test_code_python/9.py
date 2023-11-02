def solution():
     """Tina makes $18.00 an hour. If she works more than 8 hours per shift, she is eligible for overtime, which is paid by your hourly wage + 1/2 your hourly wage. If she works 10 hours every day for 5 days, how much money does she make?"""
     regular_pay = 18.00
     overtime_pay = (regular_pay * 1.5)
     overtime_hours = 2
     regular_hours = 10 - overtime_hours
     overtime_wage = (overtime_pay * overtime_hours)
     regular_wage = (regular_pay * regular_hours)
     total_hours = 50
     total_wage = (overtime_wage + regular_wage)
     result = total_wage
     
     return result

print(solution())