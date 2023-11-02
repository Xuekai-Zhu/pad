def solution():
    num_years = 14

    # Calculate the total number of episodes in 8 seasons with 15 episodes each
    num_episodes_season1 = 8 * 15

    # Calculate the total number of episodes in 4 seasons with 20 episodes each
    num_episodes_season2 = 4 * 20

    # Calculate the total number of episodes in 2 seasons with 12 episodes each
    num_episodes_season3 = 2 * 12

    # Calculate the total number of episodes in all seasons
    total_num_episodes = num_episodes_season1 + num_episodes_season2 + num_episodes_season3

    # Calculate the average number of episodes per year
    avg_num_episodes_per_year = total_num_episodes / num_years
    result = avg_num_episodes_per_year
    return result

print(solution())