def solution():
    current_height_inches = 180  # The current height of the tree in inches
    growth_percentage = 50  # The tree has grown 50% taller than it was when planted

    # Calculate the original height of the tree
    original_height_inches = current_height_inches / (1 + (growth_percentage / 100))
    original_height_feet = original_height_inches / 12  # Convert the original height from inches to feet
    result = original_height_feet
    return result

print(solution())