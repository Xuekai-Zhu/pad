def solution():
    """There are three times as many hogs as cats in King Henry's kingdom. If there are 75 hogs, what's 5 less than 60% of the number of cats in King Henry's kingdom?"""
    # Calculate the number of cats in the kingdom
    hogs_to_cats_ratio = 3
    num_hogs = 75
    num_cats = num_hogs / hogs_to_cats_ratio

    # Calculate 60% of the number of cats and subtract 5
    result = 0.6 * num_cats - 5
    return result

print(solution())