def solution():
     total_sales = 80
     total_necklaces = 4
     total_rings = 8
     necklace_cost = 12
     ring_cost = (total_sales - (total_necklaces * necklace_cost)) / total_rings
     result = ring_cost
     return result

print(solution())