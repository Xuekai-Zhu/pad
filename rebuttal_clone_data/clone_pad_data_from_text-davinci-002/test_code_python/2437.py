def solution():
     initial_amount = 100
     daily_expense = 8
     total_expense = daily_expense * 7
     remaining_amount = initial_amount - total_expense
     five_bills = remaining_amount // 5
     remaining_amount = remaining_amount % 5
     result = remaining_amount
     return result

print(solution())