def solution():
    """If Kingsley's teacher instructed her to find four friends to help her carry some chairs to the school hall to be used for an upcoming event. If each student carried 5 chairs per trip and made 10 trips in total, what's the total number of chairs taken to the hall?"""
    num_friends = 4
    chairs_per_trip = 5
    num_trips = 10
    total_chairs = num_friends * chairs_per_trip * num_trips
    result = total_chairs
    return result

print(solution())