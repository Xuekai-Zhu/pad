def solution():
    """Travis and his brother joined a trick-or-treat event. They collected 68 pieces of candy altogether. Each of them ate 4 pieces of candy after the event. How many pieces of candy were left?"""
    candy_collected = 68
    candy_eaten = 4 * 2
    candy_left = candy_collected - candy_eaten
    result = candy_left
    return result

print(solution())