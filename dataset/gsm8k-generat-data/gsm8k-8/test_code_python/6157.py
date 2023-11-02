def solution():
    # Calculate the number of audience members who disappeared
    disappeared = 100

    # Calculate the number of times an audience member did not reappear
    never_reappeared = disappeared * 0.1

    # Calculate the number of times two people reappeared
    two_reappeared = disappeared * 0.05

    # Calculate the number of times one person reappeared
    one_reappeared = disappeared - never_reappeared - two_reappeared

    # Calculate the total number of people who reappeared
    total_reappeared = one_reappeared + (2 * two_reappeared)

    result = total_reappeared
    return result

print(solution())