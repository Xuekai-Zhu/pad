def solution():
    """One dress requires 5.5 yards of fabric. Amare needs to make 4 dresses for the wedding and she has 7 feet of fabric. How many feet of fabric does Amare still need for the dresses?"""
    yards_per_dress = 5.5
    dresses_needed = 4
    total_yards_needed = yards_per_dress * dresses_needed
    feet_per_yard = 3
    total_feet_needed = total_yards_needed * feet_per_yard
    fabric_left = 7
    fabric_needed = total_feet_needed - fabric_left
    result = fabric_needed
    return result

print(solution())