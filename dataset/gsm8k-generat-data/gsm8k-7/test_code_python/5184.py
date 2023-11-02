def solution():
    fabric_per_pant = 8.5
    pants_needed = 7
    fabric_per_yard = 3

    # Convert 3.5 yards to feet
    fabric_available = 3.5 * fabric_per_yard * 12

    # Calculate the total fabric needed for all pants
    total_fabric_needed = pants_needed * fabric_per_pant

    # Calculate the fabric still needed after using the available fabric
    fabric_still_needed = total_fabric_needed - fabric_available

    result = fabric_still_needed
    return result

print(solution())