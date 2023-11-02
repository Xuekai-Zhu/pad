def solution():
    """There are three times as many hogs as cats in King Henry's kingdom. If there are 75 hogs, what's 5 less than 60% of the number of cats in King Henry's kingdom?"""
    # Number of hogs
    hogs = 75
    # Number of cats
    cats = hogs / 3
    # 60% of cats
    cats_60 = 0.6 * cats
    # 5 less than 60% of cats
    result = cats_60 - 5
    return result

print(solution())