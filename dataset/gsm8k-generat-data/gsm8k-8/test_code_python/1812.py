def solution():
    total_travel_time = 9
    time_spent_reading = 2
    time_spent_eating = 1
    time_spent_watching_movies = 3

    time_left_for_nap = total_travel_time - time_spent_reading - time_spent_eating - time_spent_watching_movies
    result = time_left_for_nap
    return result

print(solution())