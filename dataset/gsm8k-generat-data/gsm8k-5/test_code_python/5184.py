def solution():
    feet_per_yard = 3  # There are 3 feet per yard
    pants_per_yard = 3.5 / 8.5  # Nguyen can make 3.5 pants per yard of fabric
    total_pants = 7  # Nguyen needs to make 7 pairs of pants
    fabric_needed = total_pants * 8.5  # Nguyen needs 8.5 feet of fabric per pair of pants

    # Calculate the total fabric needed in yards
    fabric_needed_yards = fabric_needed / feet_per_yard

    # Calculate the fabric still needed in yards
    fabric_still_needed_yards = fabric_needed_yards - 3.5

    # Convert the fabric still needed to feet
    fabric_still_needed_feet = fabric_still_needed_yards * feet_per_yard
    result = fabric_still_needed_feet
    return result

print(solution())