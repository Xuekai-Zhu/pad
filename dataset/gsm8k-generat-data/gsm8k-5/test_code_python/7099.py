def solution():
    skips_per_second = 3  # Matt skips ropes 3 times per second
    seconds_per_minute = 60  # There are 60 seconds in a minute
    minutes = 10  # Matt jumped rope for 10 minutes

    # Calculate the total number of skips
    total_skips = skips_per_second * seconds_per_minute * minutes

    result = total_skips
    return result

print(solution())