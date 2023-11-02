def solution():
    # Calculate the total number of skips for each throw
    throw1_skips = 1
    throw2_skips = throw1_skips + 2
    throw3_skips = throw2_skips * 2
    throw4_skips = throw3_skips - 3
    throw5_skips = 8
    total_skips = throw1_skips + throw2_skips + throw3_skips + throw4_skips + throw5_skips
    result = total_skips
    return result

print(solution())