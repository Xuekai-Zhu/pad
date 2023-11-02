def solution():
     price_per_meter = 0.2
     fences = 50
     length_of_fence = 500
     total_meters = fences * length_of_fence
     total_price = total_meters * price_per_meter
     result = total_price
     return result

print(solution())