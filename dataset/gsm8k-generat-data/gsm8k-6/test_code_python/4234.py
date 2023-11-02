def solution():
    # Calculate the number of cats in King Henry's kingdom
    hogs_cats_ratio = 3  # hogs:cats ratio is 3:1
    hogs = 75  # given that there are 75 hogs
    cats = hogs // hogs_cats_ratio  # calculate the number of cats based on the ratio
    cats_60_percent = 0.6 * cats  # calculate 60% of the number of cats
    result = cats_60_percent - 5  # subtract 5 from 60% of the number of cats
    return result

print(solution())