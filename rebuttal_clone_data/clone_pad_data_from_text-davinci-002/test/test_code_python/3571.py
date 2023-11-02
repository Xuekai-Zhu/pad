def solution():
     money = 480
     money_spent_on_food = money / 2
     money_left = money - money_spent_on_food
     money_spent_on_glasses = money_left / 3
     money_left = money_left - money_spent_on_glasses
     result = money_left
     return result

print(solution())