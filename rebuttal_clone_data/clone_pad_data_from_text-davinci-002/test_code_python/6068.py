def solution():
     initial_money = 25
     money_given = 8
     money_invested = (initial_money - money_given) / 2
     money_spent = 5 * 0.50
     final_money = initial_money - money_given - money_invested - money_spent
     result = final_money
     return result

print(solution())