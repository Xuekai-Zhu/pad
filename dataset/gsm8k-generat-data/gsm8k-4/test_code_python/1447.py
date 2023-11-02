def solution():
    """Mary and Ann are going sledding. Mary slides down a hill that's 630 feet long at a speed of 90 feet/minute. Ann slides down a hill that's 800 feet long at a rate of 40 feet/minute. How much longer does Ann's trip take than Mary?"""
    # Calculate the time it takes Mary to slide down the hill
    mary_time = 630 / 90

    # Calculate the time it takes Ann to slide down the hill
    ann_time = 800 / 40

    # Calculate the difference in time between Ann and Mary
    time_diff = ann_time - mary_time

    # Return the result in minutes
    result = time_diff
    return result

print(solution())