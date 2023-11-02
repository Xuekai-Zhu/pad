def solution():
    # Calculate the number of water balloons Max fills up
    max_time = 30
    max_rate = 2
    max_filled = max_time * max_rate

    # Calculate the number of water balloons Zach fills up
    zach_time = 40
    zach_rate = 3
    zach_filled = zach_time * zach_rate

    # Calculate the total number of filled water balloons
    total_filled = max_filled + zach_filled - 10

    result = total_filled
    return result

print(solution())