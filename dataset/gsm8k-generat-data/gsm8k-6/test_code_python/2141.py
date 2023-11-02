def solution():
    # Calculate the time it takes to mow 3/4 of 8 acres with the riding mower
    riding_mower_time = (3/4) * 8 / 2  # 2 acres cut per hour

    # Calculate the time it takes to mow 1/4 of 8 acres with the push mower
    push_mower_time = (1/4) * 8 / 1  # 1 acre cut per hour

    # Calculate the total time Jerry spends mowing each week
    total_mowing_time = riding_mower_time + push_mower_time

    result = total_mowing_time
    return result

print(solution())