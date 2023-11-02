def solution():
     initial_nuts = 30
     eaten_nuts = 5
     total_nuts = 6
     left_nuts = (total_nuts - eaten_nuts) / total_nuts * initial_nuts
     result = left_nuts
     
     return result

print(solution())