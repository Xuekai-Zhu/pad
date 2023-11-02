def solution():
    num_episodes = 20
    episode_length = 30 # in minutes
    num_days = 5

    # Calculate the total length of all episodes in minutes
    total_length_in_minutes = num_episodes * episode_length

    # Convert total length to hours
    total_length_in_hours = total_length_in_minutes / 60

    # Calculate the number of hours John has to watch per day
    hours_per_day = total_length_in_hours / num_days

    result = hours_per_day
    return result

print(solution())