def solution():
    jumps_per_minute_child = 30  # Bobby could jump rope 30 times per minute as a child
    jumps_per_minute_adult = 60  # Bobby can jump 60 times per minute as an adult

    # Calculate the difference in jumps per minute between when Bobby was a child and now that he is an adult
    difference_jumps_per_minute = jumps_per_minute_adult - jumps_per_minute_child

    # Calculate the difference in jumps over a 1-minute period
    difference_jumps_per_second = difference_jumps_per_minute / 60

    # Calculate the difference in jumps over a 1-hour period
    difference_jumps_per_hour = difference_jumps_per_second * 3600

    result = difference_jumps_per_hour
    return result

print(solution())