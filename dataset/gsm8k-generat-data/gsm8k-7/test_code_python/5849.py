def solution():
    # Total number of weekdays in a week
    num_weekdays = 5
    # Length of each episode in hours
    episode_length_hours = 0.5

    # Calculate total length of show Max watched
    total_length_hours = (num_weekdays - 1) * episode_length_hours

    result = total_length_hours
    return result

print(solution())