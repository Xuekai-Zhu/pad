def solution():
    total_travel_time = 9
    book_time = 2
    dinner_time = 1
    movie_time = 3

    # Calculate the total time Bret spends on activities
    total_activity_time = book_time + dinner_time + movie_time

    # Calculate the time Bret has left for a nap
    nap_time = total_travel_time - total_activity_time
    result = nap_time
    return result

print(solution())