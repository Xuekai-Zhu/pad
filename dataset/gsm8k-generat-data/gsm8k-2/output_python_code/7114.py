def solution():
    """Jake trips over his dog 40% percent of mornings. 25% of the time he trips, he drops his coffee. What percentage of mornings does he NOT drop his coffee?"""
    trip_freq = 0.4
    drop_coffee_freq = 0.25 * trip_freq
    not_drop_coffee_freq = 1 - drop_coffee_freq
    result = not_drop_coffee_freq * 100
    return result

print(solution())