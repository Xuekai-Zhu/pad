def solution():
    """Kevin has a tree growing in his garden that is currently 180 inches tall. That is 50% taller than it was when he planted it there. How tall was the tree, in feet, then?"""
    # Define the current height of the tree in inches
    current_height = 180

    # Calculate the original height of the tree in inches
    original_height = current_height / 1.5

    # Convert the original height from inches to feet
    original_height_feet = original_height / 12

    result = original_height_feet
    return result

print(solution())