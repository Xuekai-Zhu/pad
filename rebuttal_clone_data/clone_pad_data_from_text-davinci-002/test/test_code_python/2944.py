def solution():
    feet_per_pair = 8.5
    pairs_needed = 7
    total_feet = feet_per_pair * pairs_needed
    yards_owned = 3.5
    feet_per_yard = 3
    total_feet_owned = yards_owned * feet_per_yard
    feet_needed = total_feet - total_feet_owned
    result = feet_needed
    
    return result

print(solution())