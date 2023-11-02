def solution():
    # Define the number of episodes in the first and second half of the season
    first_half_episodes = 22 // 2
    second_half_episodes = 22 - first_half_episodes

    # Calculate the cost of the first half of the season
    first_half_cost = first_half_episodes * 1000

    # Calculate the cost of the second half of the season
    second_half_cost = second_half_episodes * (1000 * 1.2)

    # Calculate the total cost of the season
    season_cost = first_half_cost + second_half_cost
    result = season_cost
    return result

print(solution())