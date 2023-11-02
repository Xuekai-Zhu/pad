def solution():
    # Calculate the total number of skips Matt made in 10 minutes
    total_skips = 3 * 60 * 10  # Matt skips 3 times per second, so in 1 minute, he skips 3 x 60 = 180 times, in 10 minutes, he skips 180 x 10 = 1800 times
    result = total_skips
    return result

print(solution())