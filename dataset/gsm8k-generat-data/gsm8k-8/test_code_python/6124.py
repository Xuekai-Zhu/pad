def solution():
    # Convert yards to feet
    fabric_per_dress = 5.5 * 3

    # Calculate total fabric needed for 4 dresses
    total_fabric_needed = fabric_per_dress * 4

    # Convert total fabric needed to feet
    total_fabric_needed_feet = total_fabric_needed / 12

    # Calculate how much fabric Amare still needs
    fabric_still_needed = total_fabric_needed_feet - 7

    result = fabric_still_needed
    return result

print(solution())