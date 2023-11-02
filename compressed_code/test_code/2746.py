def solution():
    
    quilts_per_yard = 7
    yards_for_quilts = 21
    quilts_needed = 12
    yards_needed = (quilts_needed * yards_for_quilts) / quilts_per_yard
    result = yards_needed
    return result

print(solution())