def solution():
     percent_spent = 35
     money_spent = 14
     allowance = money_spent / (percent_spent / 100)
     money_left = allowance - money_spent
     result = money_left
     return result

print(solution())