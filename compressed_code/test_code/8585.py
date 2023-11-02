def solution():
    
    quilts_per_yard = 7
    yards_for_quilts = 21
    quilts_needed = 12
    yards_needed = (quilts_needed / quilts_per_yard) * yards_for_quilts
    result = yards_needed
    return result

print(solution())