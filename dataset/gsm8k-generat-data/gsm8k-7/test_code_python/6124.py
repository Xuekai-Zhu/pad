def solution():
    yards_per_dress = 5.5
    dresses = 4
    yards_available = 7 * 3  # 1 yard = 3 feet

    # Calculate the total yards of fabric needed for all dresses
    total_yards_needed = yards_per_dress * dresses

    # Convert the total yards needed to feet
    feet_needed = total_yards_needed * 3

    # Calculate the remaining feet of fabric needed
    remaining_feet = feet_needed - yards_available
    result = remaining_feet / 3  # Convert the answer back to yards
    return result

print(solution())