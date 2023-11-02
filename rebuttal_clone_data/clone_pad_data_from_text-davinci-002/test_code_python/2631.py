def solution():
     shirts_made = 3
     pants_made = 5
     fabric_per_shirt = 2
     fabric_per_pants = 5
     total_fabric = (shirts_made * fabric_per_shirt) + (pants_made * fabric_per_pants)
     yards_needed = total_fabric / 3
     result = yards_needed
     return result

print(solution())