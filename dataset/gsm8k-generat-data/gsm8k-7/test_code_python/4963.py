def solution():
    first_season_cost = 100000 * 12  # cost of 12 episodes in the first season
    total_cost = first_season_cost

    # for each of the other 4 seasons, calculate the cost and add it to the total cost
    for season in range(2, 6):
        if season != 5:
            episodes = round(12 * (1.5 ** (season-1)))  # calculate the number of episodes
        else:
            episodes = 24
        cost_per_episode = 100000 * 2**(season-1)  # calculate the cost per episode
        season_cost = episodes * cost_per_episode  # calculate the total cost of the season
        total_cost += season_cost  # add the season cost to the total cost

    result = total_cost
    return result

print(solution())