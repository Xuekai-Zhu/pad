def solution():
     car_washes_per_month = 20
     dog_walks_per_month = 40
     savings_goal = 150
     monthly_savings = (car_washes_per_month + dog_walks_per_month) / 2
     months_needed = savings_goal / monthly_savings
     result = months_needed
     return result

print(solution())