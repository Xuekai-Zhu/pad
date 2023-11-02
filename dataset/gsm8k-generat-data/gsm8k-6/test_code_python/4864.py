def solution():
    # Calculate the time to knit all the items for one grandchild
    time_per_child = 2 + 3 + 2*1 + 2*(1.5) + 6  # time to knit hat + time to knit scarf + time to knit mittens (2) + time to knit socks (2) + time to knit sweater
    # Calculate the time to knit all the items for three grandchildren
    total_time = time_per_child * 3
    result = total_time
    return result

print(solution())