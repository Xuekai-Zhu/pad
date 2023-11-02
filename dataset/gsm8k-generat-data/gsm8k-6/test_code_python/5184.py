def solution():
    # Convert yards to feet
    available_fabric = 3.5 * 3  # 1 yard = 3 feet

    # Calculate the total length of fabric required for 7 pairs of pants
    total_fabric_required = 7 * 8.5

    # Calculate the amount of fabric still needed
    fabric_still_needed = total_fabric_required - available_fabric

    result = fabric_still_needed
    return result

print(solution())