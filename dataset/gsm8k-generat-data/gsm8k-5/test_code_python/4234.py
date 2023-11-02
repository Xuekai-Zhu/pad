def solution():
    hogs = 75  # There are 75 hogs in King Henry's kingdom
    cats = hogs / 3  # There are three times as many hogs as cats
    cats_percentage = 60  # We need to find 60% of the number of cats

    # Calculate the number of cats
    cats_number = cats_percentage / 100 * cats

    # Calculate 5 less than 60% of the number of cats
    result = cats_number * 0.6 - 5
    return result

print(solution())