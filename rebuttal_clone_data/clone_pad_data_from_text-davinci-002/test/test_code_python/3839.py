def solution():
     cost_small = 3
     cost_large = 5
     money = 50
     small_glasses = 8
     total_cost = cost_small * small_glasses
     large_glasses = (money - total_cost - 1) / cost_large
     result = large_glasses
     return result

print(solution())