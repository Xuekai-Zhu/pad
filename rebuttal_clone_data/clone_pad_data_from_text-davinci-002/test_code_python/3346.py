def solution():
     money_spent_september = 1/5
     money_spent_october = 1/4
     money_spent_november = 120
     money_left = 540
     total_money_spent = money_spent_september + money_spent_october + money_spent_november
     initial_amount = money_left + total_money_spent
     result = initial_amount
     return result

print(solution())