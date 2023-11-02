def solution():
    # Convert yards to feet
    total_fabric = 3.5 * 3

    # Calculate how much fabric is needed for all 7 pants
    pants_fabric = 7 * 8.5

    # Calculate how much fabric is still needed
    remaining_fabric = pants_fabric - total_fabric

    result = remaining_fabric
    return result

print(solution())