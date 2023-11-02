def solution():
    total_flight_time = 10 * 60  # The total flight time is 10 hours, converted to minutes

    # Calculate the time Emily spends watching TV shows
    tv_time = 3 * 25  # Emily watches 3 TV episodes that are 25 minutes each

    # Calculate the time Emily spends sleeping
    sleep_time = 4.5 * 60  # Emily sleeps for 4 and a half hours, converted to minutes

    # Calculate the time Emily spends watching movies
    movie_time = 2 * 105  # Emily watches 2 movies that are each 1 hour and 45 minutes long, so 105 minutes each

    # Calculate the total time Emily spends on activities
    total_activity_time = tv_time + sleep_time + movie_time

    # Calculate the remaining time in the flight
    remaining_time = total_flight_time - total_activity_time
    result = remaining_time
    return result

print(solution())