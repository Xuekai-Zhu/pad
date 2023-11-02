def solution():
    # Convert the current height to inches
    current_height = 180

    # Calculate the original height of the tree in inches
    original_height = current_height / 1.5

    # Convert the original height to feet
    original_height_feet = original_height / 12

    result = original_height_feet
    return result

print(solution())