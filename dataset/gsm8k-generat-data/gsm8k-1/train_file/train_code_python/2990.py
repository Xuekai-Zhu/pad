def solution():
    """A total of 107 oranges are picked by Del and Juan. Del picked 23 on each of 2 days and Juan picked the rest. How many oranges did Juan pick?"""
    total_oranges = 107
    del_oranges = 23 * 2
    juan_oranges = total_oranges - del_oranges
    result = juan_oranges
    return result

print(solution())