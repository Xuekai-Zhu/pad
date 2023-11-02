def solution():
    movie_length = 1.5  # The movie is 1.5 hours long
    replays_per_day = 6  # The movie is replayed 6 times per day
    advertisement_length = 20 / 60  # The advertisement is 20 minutes long, converted to hours

    # Calculate the total time the movie is shown per day, including advertisements
    total_time = (movie_length + advertisement_length) * replays_per_day

    result = total_time
    return result

print(solution())