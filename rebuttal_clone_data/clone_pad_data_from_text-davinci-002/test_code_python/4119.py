def solution():
     initial_amount = 350
     second_month = initial_amount * 2 + 50
     third_month = second_month * 2 + initial_amount
     total = initial_amount + second_month + third_month
     result = total
     return result

print(solution())