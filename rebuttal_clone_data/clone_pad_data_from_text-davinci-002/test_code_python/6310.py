def solution():
     combined_weight = 158
     tracy_weight = 52
     jake_weight = 8
     john_weight = combined_weight - tracy_weight - jake_weight
     min_weight = min(tracy_weight, john_weight, jake_weight)
     max_weight = max(tracy_weight, john_weight, jake_weight)
     range_weight = max_weight - min_weight
     
     return range_weight

print(solution())