def solution():
    BAKERY_1_NEEDS = 2
    BAKERY_2_NEEDS = 4
    BAKERY_3_NEEDS = 12
    NUM_WEEKS = 4

    # Calculate the total number of sacks needed for all the bakeries
    total_sacks_needed = (BAKERY_1_NEEDS + BAKERY_2_NEEDS + BAKERY_3_NEEDS) * NUM_WEEKS
    result = total_sacks_needed
    return result

print(solution())