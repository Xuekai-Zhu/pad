def solution():
    # Calculate the total time spent watching movies
    total_time_movies = 1.5 * 2  # both movies are an average length of 1.5 hours

    # Convert total time spent watching movies to minutes and subtract from total time available
    total_time_running = (24*60) - (total_time_movies*60)

    # Calculate the distance run by Paul
    distance_run = total_time_running / 12  # Paul can run a mile in 12 minutes

    result = distance_run
    return result

print(solution())