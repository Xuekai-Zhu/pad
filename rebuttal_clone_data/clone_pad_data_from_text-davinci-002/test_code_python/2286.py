def solution():
     money_collected = 240
     hourly_pay = 10
     total_tips = 50
     total_income = money_collected + total_tips
     hours_worked = total_income / hourly_pay
     result = hours_worked
     return result

print(solution())