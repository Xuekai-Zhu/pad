def solution():
    num_hogs = 75

    # Calculate the number of cats in the kingdom
    num_cats = num_hogs / 3

    # Calculate 60% of the number of cats and subtract 5
    result = 0.6 * num_cats - 5
    return result

print(solution())