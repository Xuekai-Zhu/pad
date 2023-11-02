def solution():
    # Define variables
    rajesh_distance = 0
    hiro_distance = 0
    total_distance = 25

    # Set up equation system
    # rajesh_distance = 4 * hiro_distance - 10
    # rajesh_distance + hiro_distance = total_distance

    # Solve for rajesh_distance
    hiro_distance = (total_distance + 10) / 5
    rajesh_distance = 4 * hiro_distance - 10
    result = rajesh_distance
    return result

print(solution())