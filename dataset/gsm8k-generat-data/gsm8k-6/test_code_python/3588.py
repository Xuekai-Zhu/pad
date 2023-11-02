def solution():
    # We want to find the initial number of bedbugs, so we need to work backwards from the final count of 810 after 4 days.

    # First, we will find the number of bedbugs after 3 days by dividing the final count by 3 three times.
    bedbugs_after_3_days = 810 / 3 / 3 / 3

    # Next, we will find the number of bedbugs after 2 days, which is equal to the number after 3 days divided by 3.
    bedbugs_after_2_days = bedbugs_after_3_days / 3

    # Similarly, we will find the number after 1 day, which is equal to the number after 2 days divided by 3.
    bedbugs_after_1_day = bedbugs_after_2_days / 3

    # Finally, we will find the initial number of bedbugs, which is equal to the number after 1 day divided by 3.
    initial_bedbugs = bedbugs_after_1_day / 3

    result = initial_bedbugs
    return result

print(solution())