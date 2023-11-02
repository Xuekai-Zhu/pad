def solution():
     shoes_cost = 200
     shirts_cost = 80
     discount_shoes = shoes_cost * (30 / 100)
     discount_shirts = shirts_cost * (5 / 100)
     total_discount = discount_shoes + discount_shirts
     total_cost = shoes_cost + shirts_cost - total_discount
     result = total_cost
     return result

print(solution())