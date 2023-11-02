def solution():
     t_shirt = 30
     backpack = 10
     cap = 5
     total_spent = 43
     total_without_discount = t_shirt + backpack + cap
     discount = total_without_discount - total_spent
     result = discount
     return result

print(solution())