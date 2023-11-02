def solution():
     hourly_rate = 30
     hours_worked = 18
     late_fee = 5
     number_of_times_late = 3
     total_fees = late_fee * number_of_times_late
     gross_pay = hourly_rate * hours_worked
     net_pay = gross_pay - total_fees
     result = net_pay
     
     return result

print(solution())