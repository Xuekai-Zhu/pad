def solution():
     weekly_rate = 280
     monthly_rate = 1000
     weeks_in_month = 4
     months = 3
     weekly_total = weekly_rate * weeks_in_month * months
     monthly_total = monthly_rate * months
     savings = monthly_total - weekly_total
     result = savings
     return result

print(solution())