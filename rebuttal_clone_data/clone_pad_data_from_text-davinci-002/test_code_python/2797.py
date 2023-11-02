def solution():
     daily_expenses = 4000
     salary_expenses = daily_expenses * 2/5
     delivery_expenses = (daily_expenses - salary_expenses) * 1/4
     order_expenses = daily_expenses - salary_expenses - delivery_expenses
     result = order_expenses
     return result

print(solution())