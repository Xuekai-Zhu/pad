def solution():
    """Larry and Barry want to pick apples out of the tree, but neither is tall enough to reach the apples.  Barry can reach apples that are 5 feet high.  Larry is 5 feet tall, but his shoulder height is 20% less than his full height.  If Barry stands on Larry's shoulders, how high can they reach?"""
    # Define the height of Barry, Larry, and Larry's shoulders
    barry_height = 5
    larry_height = 5
    larry_shoulders = larry_height - (0.2 * larry_height)

    # Calculate the total height Barry and Larry can reach
    total_height = barry_height + larry_shoulders

    # Return the result
    result = total_height
    return result

print(solution())