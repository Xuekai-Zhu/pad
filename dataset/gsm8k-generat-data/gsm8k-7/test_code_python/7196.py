def solution():
    flight_time = 11.33      # in hours
    reading_time = 2         # in hours
    movie_time = 4           # in hours
    dinner_time = 0.5        # in hours
    radio_time = 0.67        # in hours
    games_time = 1.17        # in hours

    # Calculate the total amount of time spent on non-nap activities
    non_nap_time = reading_time + movie_time + dinner_time + radio_time + games_time

    # Calculate the amount of time left for napping
    nap_time = flight_time - non_nap_time

    result = nap_time
    return result

print(solution())