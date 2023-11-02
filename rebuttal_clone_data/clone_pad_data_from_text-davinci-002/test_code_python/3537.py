def solution():
     quilts_made = 7
     yards_of_material = 21
     quilts_needed = 12
     yards_needed = (quilts_needed / quilts_made) * yards_of_material
     result = yards_needed
     return result

print(solution())