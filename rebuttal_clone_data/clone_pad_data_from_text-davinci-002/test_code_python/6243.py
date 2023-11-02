def solution():
     cost_of_food = 50
     service_fee = 12
     tip = 5
     total_cost = cost_of_food + (cost_of_food * (service_fee / 100)) + tip
     result = total_cost
     return result

print(solution())