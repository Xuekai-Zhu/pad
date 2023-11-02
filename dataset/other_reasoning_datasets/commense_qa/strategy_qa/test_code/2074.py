def solution():
    flight_time = 4.5 # hours
    batman_runtime = 2.1 # hours
    passenger_age_group = "18-34"
    movie_rating = "PG-13"
    if batman_runtime <= flight_time and (movie_rating == "PG-13" or movie_rating == "R") and passenger_age_group == "18-34":
        result = "likely"
    else:
        result = "unlikely"
    return result

print(solution())