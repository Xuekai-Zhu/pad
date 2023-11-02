def solution():
     pounds_per_container = 45
     price_per_container = 21
     pounds_needed = 15 * 210
     containers_needed = pounds_needed / pounds_per_container
     total_cost = containers_needed * price_per_container
     result = total_cost
     return result

print(solution())