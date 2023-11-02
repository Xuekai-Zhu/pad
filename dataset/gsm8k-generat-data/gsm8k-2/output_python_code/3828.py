def solution():
    """Tina's bag contains nine apples, 5 oranges, and 17 tangerines. If she took away 2 oranges and 10 tangerines, how many more tangerines than oranges would she have left?"""
    apples = 9
    oranges = 5 - 2  # took away 2 oranges
    tangerines = 17 - 10  # took away 10 tangerines
    diff = tangerines - oranges
    result = diff
    return result

print(solution())