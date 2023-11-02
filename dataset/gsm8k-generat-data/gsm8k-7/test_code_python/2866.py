def solution():
    num_episodes = 6
    episode_length = 50  # in minutes

    # Calculate the total length of all episodes in minutes
    total_duration = num_episodes * episode_length

    # Convert total duration from minutes to hours
    total_duration_hours = total_duration / 60

    result = total_duration_hours
    return result

print(solution())