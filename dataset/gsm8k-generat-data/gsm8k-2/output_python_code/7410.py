def solution():
    """Kevin has a tree growing in his garden that is currently 180 inches tall. That is 50% taller than it was when he planted it there. How tall was the tree, in feet, then?"""
    current_height = 180
    original_height = current_height / 1.5
    height_in_feet = original_height / 12
    result = height_in_feet
    return result

print(solution())