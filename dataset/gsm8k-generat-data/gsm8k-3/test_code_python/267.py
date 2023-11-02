def solution():
    """Larry and Barry want to pick apples out of the tree, but neither is tall enough to reach the apples.  Barry can reach apples that are 5 feet high.  Larry is 5 feet tall, but his shoulder height is 20% less than his full height.  If Barry stands on Larry's shoulders, how high can they reach?"""
    # Define the height that Barry can reach
    BARRY_HEIGHT = 5

    # Calculate Larry's shoulder height
    shoulder_height = 5 * 0.8

    # Calculate the total height they can reach
    total_height = BARRY_HEIGHT + shoulder_height

    # Display the total height they can reach
    result = total_height
    return result

print(solution())