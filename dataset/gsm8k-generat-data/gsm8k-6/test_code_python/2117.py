def solution():
    # Calculate the time it takes for each friend to run 5 miles
    time_friend1 = (5/3) * 21  # distance in miles divided by rate (in miles/minute)
    time_friend2 = (5/3) * 24
    total_time = time_friend1 + time_friend2  # add the two times together
    result = total_time
    return result

print(solution())