def solution():
     cost_small = 8
     cost_large = 12
     num_small = 3
     num_large = 1
     total_cost = (cost_small * num_small) + (cost_large * num_large)
     difference = 60 - total_cost
     result = difference
     return result

print(solution())