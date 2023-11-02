def solution():
     cone_price = 5
     daily_expenses = 0.8
     desired_profit = 200
     needed_sales = desired_profit / (1 - daily_expenses)
     needed_cones = needed_sales / cone_price
     result = needed_cones
     return result

print(solution())