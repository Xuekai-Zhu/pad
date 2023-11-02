def solution():
    """If a bunny comes out of its burrow 3 times per minute, calculate the combined number of times 20 bunnies at the same pace will have come out of their burrows in 10 hours."""
    bunnies = 20
    times_per_minute = 3
    minutes_per_hour = 60
    hours = 10
    total_times = bunnies * times_per_minute * minutes_per_hour * hours
    result = total_times
    return result

print(solution())