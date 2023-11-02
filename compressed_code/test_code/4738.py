def solution():
    
    yards_per_dress = 5.5
    dresses_needed = 4
    total_yards_needed = yards_per_dress * dresses_needed
    feet_per_yard = 3
    total_feet_needed = total_yards_needed * feet_per_yard
    feet_available = 7
    feet_still_needed = total_feet_needed - feet_available
    result = feet_still_needed
    return result

print(solution())