def solution():
    """A total of 107 oranges are picked by Del and Juan. Del picked 23 on each of 2 days and Juan picked the rest. How many oranges did Juan pick?"""
    del_picked = 23 * 2
    total_picked = 107
    juan_picked = total_picked - del_picked
    result = juan_picked
    return result

print(solution())