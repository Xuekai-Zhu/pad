def solution():
    """When it rains, the three holes in the garage roof leak water at different rates. The largest hole leaks at a rate of 3 ounces of water per minute. The medium-sized hole leaks water at one-half the rate of the largest hole. And the smallest hole leaks water at a rate of one-third the rate of the medium-sized hole. When it rains, what is the combined amount of water, in ounces, that leak from all three holes over a 2-hour time period?"""
    largest_rate = 3
    medium_rate = largest_rate / 2
    smallest_rate = medium_rate / 3
    total_rate = largest_rate + medium_rate + smallest_rate
    time_in_minutes = 2 * 60
    total_water_leaked = total_rate * time_in_minutes
    result = total_water_leaked
    return result

print(solution())