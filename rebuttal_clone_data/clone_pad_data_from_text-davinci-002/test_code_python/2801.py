def solution():
     total_legs = 1100
     legs_seen = 12 + 8 + 5
     legs_needed = total_legs - legs_seen
     tarantulas_needed = legs_needed / 8
     result = tarantulas_needed
     return result

print(solution())