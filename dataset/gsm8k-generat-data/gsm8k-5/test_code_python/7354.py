def solution():
    # Calculate the total number of times Helen cuts her lawn
    times_cut = (2 * 2) + (4 * 4) + (2 * 2) + (2 * 2)  # 2 times per month in March, April, September, and October. 4 times per month in May, June, July, and August.

    # Calculate the total number of gallons used
    gallons_used = (times_cut // 4) * 2  # Helen uses 2 gallons of gas every 4th time she cuts her lawn

    result = gallons_used
    return result

print(solution())