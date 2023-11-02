def solution():
     milk_price = 1.5
     fruit_price = 2
     milk_needed = 10
     fruit_needed = 3
     yogurt_batches = 3
     total_cost = (milk_needed * milk_price) + (fruit_needed * fruit_price)
     cost_per_batch = total_cost / yogurt_batches
     result = cost_per_batch
     return result

print(solution())