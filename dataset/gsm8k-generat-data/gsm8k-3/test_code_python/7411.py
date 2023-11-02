def solution():
    """Kevin has a tree growing in his garden that is currently 180 inches tall. That is 50% taller than it was when he planted it there. How tall was the tree, in feet, then?"""
    # Convert current height to inches
    current_height = 180

    # Calculate original height using the formula: original_height = (1 / 1.5) * current_height
    original_height = (1 / 1.5) * current_height

    # Convert original height to feet
    original_height_feet = original_height / 12

    # Display the original height in feet
    result = original_height_feet
    return result

print(solution())