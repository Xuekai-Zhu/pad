def solution():
    first_season_cost = 100000 * 12  # First season had 12 episodes costing $100,000 each
    total_cost = first_season_cost

    for season in range(2, 6):
        if season < 5:
            episodes = int(12 * (1.5 ** (season - 1)))  # Calculate number of episodes for each season
        else:
            episodes = 24  # Last season had 24 episodes

        cost = episodes * (100000 * (2 ** (season - 1)))  # Calculate cost for each season
        total_cost += cost

    result = total_cost
    return result

print(solution())