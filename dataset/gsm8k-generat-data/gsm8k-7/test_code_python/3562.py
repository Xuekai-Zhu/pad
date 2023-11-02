def solution():
    total_stamps = 930

    # Let KJ have x stamps, then CJ has 2x + 5 stamps and AJ has 2x stamps
    x = total_stamps / (2.5) # Total number of stamps divided among the 3 boys in 2.5x

    # Calculate the number of stamps for each boy
    kj_stamps = x
    cj_stamps = 2 * x + 5
    aj_stamps = 2 * x

    result = aj_stamps
    return result

print(solution())