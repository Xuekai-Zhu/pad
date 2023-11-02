def solution():
    """When it rains, the three holes in the garage roof leak water at different rates. The largest hole leaks at a rate of 3 ounces of water per minute. The medium-sized hole leaks water at one-half the rate of the largest hole. And the smallest hole leaks water at a rate of one-third the rate of the medium-sized hole. When it rains, what is the combined amount of water, in ounces, that leak from all three holes over a 2-hour time period?"""
    largest_rate = 3
    medium_rate = 0.5 * largest_rate
    smallest_rate = 1 / 3 * medium_rate

    total_time = 2 * 60 # since we need to calculate the amount of water that would leak over a 2-hour time period
    largest_leakage = largest_rate * total_time
    medium_leakage = medium_rate * total_time
    smallest_leakage = smallest_rate * total_time

    total_leakage = largest_leakage + medium_leakage + smallest_leakage
    result = total_leakage
    return result

print(solution())