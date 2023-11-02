def solution():
    movie_length = 1.5  # in hours
    num_replays = 6
    ad_length = 20  # in minutes

    # Convert advertisement length to hours
    ad_length_hours = ad_length / 60

    # Calculate the total length of the movie and advertisements
    total_length = movie_length + ad_length_hours

    # Calculate the total length of each replay, including the advertisements
    total_replay_length = total_length * num_replays

    result = total_replay_length
    return result

print(solution())