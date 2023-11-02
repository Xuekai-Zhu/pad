def solution():
    """A total of 107 oranges are picked by Del and Juan. Del picked 23 on each of 2 days and Juan picked the rest. How many oranges did Juan pick?"""
    # Define the number of oranges picked by Del
    del_oranges = 23 * 2

    # Calculate the number of oranges picked by Juan
    juan_oranges = 107 - del_oranges

    # return the result
    result = juan_oranges
    return result

print(solution())