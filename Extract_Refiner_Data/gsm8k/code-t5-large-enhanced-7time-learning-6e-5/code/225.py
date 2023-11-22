def solution():
    
    total_watermelons = 120
    harvested_watermelons = total_watermelons * 0.3
    remaining_watermelons = total_watermelons - harvested_watermelons
    harvested_melons = remaining_watermelons * (3/4)
    unharvested_melons = remaining_watermelons - harvested_melons
    result = unharvested_melons
    return result

print(solution())