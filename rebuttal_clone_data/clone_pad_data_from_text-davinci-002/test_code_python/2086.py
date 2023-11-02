def solution():
     necklaces = 12
     rings = 30
     bracelets = 15
     
     necklace_cost = 4
     ring_cost = 10
     bracelet_cost = 5
     
     total_cost = (necklaces - 5) * necklace_cost + (rings - 18) * ring_cost + (bracelets - 8) * bracelet_cost
     result = total_cost
     return result

print(solution())