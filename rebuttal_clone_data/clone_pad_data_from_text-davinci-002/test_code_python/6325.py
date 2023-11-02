def solution():
     money = 50
     mango_cost = 3
     mangoes = 6
     apple_juice_cost = 3
     cartons = 6
     money_spent = (mangoes * mango_cost) + (cartons * apple_juice_cost)
     money_left = money - money_spent
     result = money_left
     return result

print(solution())