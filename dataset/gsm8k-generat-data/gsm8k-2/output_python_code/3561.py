def solution():
    """CJ, KJ, and AJ collect stamps. CJ has 5 more than twice the number of stamps that KJ has, and KJ has half as many as AJ. If the three boys have 930 stamps all together, how many stamps does AJ have?"""
    total_stamps = 930
    cj_stamps = 2 * kj_stamps + 5
    kj_stamps = aj_stamps / 2
    aj_stamps = total_stamps / 1.5
    result = aj_stamps
    return result

print(solution())