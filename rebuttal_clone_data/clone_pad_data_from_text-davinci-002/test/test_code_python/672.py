def solution():
     man1_hours_day1 = 10
     man2_hours_day1 = 10
     man1_hours_day2 = 8
     man2_hours_day2 = 8
     man1_hours_day3 = 15
     man2_hours_day3 = 15
     wage_per_hour = 10
     man1_total_wage = (man1_hours_day1 + man1_hours_day2 + man1_hours_day3) * wage_per_hour
     man2_total_wage = (man2_hours_day1 + man2_hours_day2 + man2_hours_day3) * wage_per_hour
     total_amount_paid = man1_total_wage + man2_total_wage
     result = total_amount_paid
     
     return result

print(solution())