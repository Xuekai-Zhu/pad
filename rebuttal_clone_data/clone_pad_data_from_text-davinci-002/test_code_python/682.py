def solution():
     january_to_july_savings = 10
     august_to_november_savings = 15
     total_savings_goal = 150
     current_total_savings = january_to_july_savings * 7 + august_to_november_savings * 5
     december_savings = total_savings_goal - current_total_savings
     result = december_savings
     return result

print(solution())