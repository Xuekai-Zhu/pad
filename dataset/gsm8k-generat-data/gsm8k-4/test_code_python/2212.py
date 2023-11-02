def solution():
    """John starts a TV show. He pays $1000 per episode for the first half of the season. The second half of the season had episodes that cost 120% more expensive. If there are 22 episodes how much did the entire season cost?"""
    # Define the number of episodes in each half of the season
    half_season = 22 // 2

    # Calculate the cost of the episodes in the first half of the season
    first_half_cost = half_season * 1000

    # Calculate the cost of the episodes in the second half of the season
    second_half_rate = 1.2
    second_half_cost = (22 - half_season) * (1000 * second_half_rate)

    # Calculate the total cost of the entire season
    total_cost = first_half_cost + second_half_cost

    result = total_cost
    return result

print(solution())