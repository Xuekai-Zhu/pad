def solution():
    # Convert 180 inches to feet
    current_height_feet = 180 / 12

    # Find the original height of the tree
    original_height_feet = current_height_feet / 1.5  # the tree is 50% taller than its original height

    result = original_height_feet
    return result

print(solution())