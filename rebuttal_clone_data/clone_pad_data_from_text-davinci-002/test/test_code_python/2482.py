def solution():
     apples = 5
     sugar = 3
     walnuts = 0.5
     price_apples = 2
     price_sugar = price_apples - 1
     price_walnuts = 6
     total_cost = apples * price_apples + sugar * price_sugar + walnuts * price_walnuts
     result = total_cost
     return result

print(solution())