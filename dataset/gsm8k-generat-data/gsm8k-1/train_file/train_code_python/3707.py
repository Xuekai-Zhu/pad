def solution():
    """Rudy runs 5 miles at a rate of 10 minutes per mile. Later he runs 4 miles at a rate of 9.5 minutes per mile. What is the total length of time that Rudy runs?"""
    distance_1 = 5
    rate_1 = 10
    time_1 = distance_1 * rate_1
    distance_2 = 4
    rate_2 = 9.5
    time_2 = distance_2 * rate_2
    total_time = time_1 + time_2
    result = total_time
    return result

print(solution())