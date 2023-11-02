def solution():
    """Tina's bag contains nine apples, 5 oranges, and 17 tangerines. If she took away 2 oranges and 10 tangerines, how many more tangerines than oranges would she have left?"""
    starting_oranges = 5
    starting_tangerines = 17
    oranges_taken = 2
    tangerines_taken = 10
    remaining_oranges = starting_oranges - oranges_taken
    remaining_tangerines = starting_tangerines - tangerines_taken
    more_tangerines_than_oranges = remaining_tangerines - remaining_oranges
    result = more_tangerines_than_oranges
    return result

print(solution())