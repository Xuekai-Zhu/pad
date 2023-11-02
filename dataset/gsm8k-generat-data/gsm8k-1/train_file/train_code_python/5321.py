def solution():
    """Of the 3 friends, Harry has 4 times as many fish as Joe, and Joe has 8 times as many fish as Sam does. If Sam has 7 fish, how many fish does Harry have?"""
    sam_fish = 7
    joe_fish = sam_fish * 8
    harry_fish = joe_fish * 4
    result = harry_fish
    return result

print(solution())