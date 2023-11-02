def solution():
    num_episodes = 8
    episode_length = 44 # in minutes

    # Calculate the total length of the TV show in minutes
    total_length = num_episodes * episode_length

    # Calculate the length of TV watched from Monday to Friday
    watched_length = 138 + 21 + (2 * episode_length)

    # Calculate the length of TV watched over the weekend
    weekend_length = total_length - watched_length
    result = weekend_length
    return result

print(solution())