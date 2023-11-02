def solution():
    # Calculate the total number of episodes in the show
    total_episodes = 22 * 9 + 26  # 9 seasons of 22 episodes each and last season has 4 additional episodes

    # Calculate the total hours to watch all episodes
    total_hours = total_episodes * 0.5  # each episode is 0.5 hours

    result = total_hours
    return result

print(solution())