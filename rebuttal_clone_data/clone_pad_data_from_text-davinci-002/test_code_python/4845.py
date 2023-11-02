def solution():
     cost_shirt = 1/3
     cost_wallet = cost_shirt + 60
     cost_food = cost_wallet - 30
     total_cost = cost_shirt + cost_wallet + cost_food
     result = total_cost
     return result

print(solution())