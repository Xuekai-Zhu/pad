def solution():
     dress_cost = 80
     savings = 20
     allowance = 30
     weekend_expenses = 10
     money_needed = dress_cost - savings
     weekly_money_needed = money_needed - weekend_expenses
     number_of_weeks = weekly_money_needed / allowance
     
     return number_of_weeks

print(solution())