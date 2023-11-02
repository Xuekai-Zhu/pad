def solution():
    total_minutes = 4 * 60  # 4 hours = 240 minutes

    # Calculate the total minutes of the first three episodes
    first_three_episodes = 58 + 62 + 65

    # Calculate the length of the fourth episode in minutes
    fourth_episode = total_minutes - first_three_episodes

    result = fourth_episode
    return result

print(solution())