def solution():
     money_left = 51
     money_spent_1 = money_left / 2
     money_spent_2 = money_spent_1 / 2
     initial_amount = money_left + money_spent_1 + money_spent_2
     result = initial_amount
     return result

print(solution())