def solution():
     total_cost = 48
     number_large_tubs = 3
     number_small_tubs = 6
     cost_large_tubs = number_large_tubs * 6
     cost_small_tubs = total_cost - cost_large_tubs
     price_small_tubs = cost_small_tubs / number_small_tubs
     result = price_small_tubs
     
     return result

print(solution())