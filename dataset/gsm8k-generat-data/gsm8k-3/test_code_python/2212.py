def solution():
    """John starts a TV show.  He pays $1000 per episode for the first half of the season.  The second half of the season had episodes that cost 120% more expensive.  If there are 22 episodes how much did the entire season cost?"""
    # Define the number of episodes in the first and second half of the season
    first_half_episodes = 11
    second_half_episodes = 11

    # Define the cost of each episode in the first half of the season and calculate the total cost
    first_half_cost = first_half_episodes * 1000
    # Define the cost increase in the second half of the season
    cost_increase = 1.20
    # Define the cost of each episode in the second half of the season and calculate the total cost
    second_half_cost = second_half_episodes * 1000 * cost_increase

    # Calculate the total cost of the entire season
    total_cost = first_half_cost + second_half_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())