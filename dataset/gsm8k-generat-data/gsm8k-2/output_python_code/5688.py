def solution():
    """If a bunny comes out of its burrow 3 times per minute, calculate the combined number of times 20 bunnies at the same pace will have come out of their burrows in 10 hours."""
    bunnies = 20
    rate = 3
    minutes_in_hour = 60
    minutes_in_10_hours = 10 * 60 * minutes_in_hour
    total_bunny_outings = bunnies * rate * minutes_in_10_hours
    result = total_bunny_outings
    return result

print(solution())