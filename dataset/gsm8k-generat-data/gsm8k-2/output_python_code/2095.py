def solution():
    """Beth went shopping. She bought 15 more cans of peas than twice the number of cans of corn that she bought. If she bought 35 cans of peas, how many cans of corn did she buy?"""
    peas = 35
    twice_corn = (peas - 15) / 2
    corn = twice_corn / 2
    result = corn
    return result

print(solution())