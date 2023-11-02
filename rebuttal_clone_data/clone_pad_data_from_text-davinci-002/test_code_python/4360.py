def solution():
     price_butter = 2 * price_bread
     price_cheese = price_butter * 1.25
     price_tea = 2 * price_cheese
     total_cost = price_butter + price_bread + price_cheese + price_tea
     result = total_cost
     return result

print(solution())