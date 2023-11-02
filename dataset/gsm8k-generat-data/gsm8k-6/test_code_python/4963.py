def solution():
    # Calculate the cost of the first season
    cost_first_season = 100000 * 12

    # Calculate the cost of the remaining 4 seasons
    cost_remaining_seasons = 0
    for i in range(2, 6):  # start from the 2nd season to the 5th season
        if i == 5:
            episodes = 24  # the last season had 24 episodes
        else:
            episodes = round(12 * (1.5 ** (i-1)))  # calculate the number of episodes with 50% increase
        cost_remaining_seasons += 2 * 100000 * episodes  # cost is twice as much as the first season

    # Calculate the total cost of all the episodes
    total_cost = cost_first_season + cost_remaining_seasons
    result = total_cost
    return result

print(solution())