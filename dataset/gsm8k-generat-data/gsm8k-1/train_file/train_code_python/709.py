def solution():
    """Travis and his brother joined a trick-or-treat event. They collected 68 pieces of candy altogether. Each of them ate 4 pieces of candy after the event. How many pieces of candy were left?"""
    total_candy_collected = 68
    candy_eaten_by_each = 4
    total_candy_eaten = candy_eaten_by_each * 2
    candy_left = total_candy_collected - total_candy_eaten
    result = candy_left
    return result

print(solution())