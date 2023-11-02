def solution():
    yards_per_dress = 5.5  # One dress requires 5.5 yards of fabric
    dresses_needed = 4  # Amare needs to make 4 dresses
    total_yards_needed = yards_per_dress * dresses_needed  # Total yards of fabric needed for all dresses
    total_feet_needed = total_yards_needed * 3  # Convert yards to feet
    available_feet = 7  # Amare has 7 feet of fabric

    # Calculate the remaining feet of fabric needed
    remaining_feet_needed = total_feet_needed - available_feet
    result = remaining_feet_needed
    return result

print(solution())