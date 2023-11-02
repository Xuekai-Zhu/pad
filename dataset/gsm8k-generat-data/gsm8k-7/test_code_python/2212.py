def solution():
    num_episodes = 22
    cost_per_episode_first_half = 1000
    cost_per_episode_second_half = cost_per_episode_first_half * 1.2

    # Calculate the total cost for the first half of the season
    total_cost_first_half = (num_episodes / 2) * cost_per_episode_first_half

    # Calculate the total cost for the second half of the season
    total_cost_second_half = (num_episodes / 2) * cost_per_episode_second_half

    # Calculate the total cost for the entire season
    total_cost = total_cost_first_half + total_cost_second_half
    result = total_cost
    return result

print(solution())