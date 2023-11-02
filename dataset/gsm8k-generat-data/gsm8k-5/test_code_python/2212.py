def solution():
    episodes = 22  # There are 22 episodes in the season
    cost_first_half = 1000 * (episodes // 2)  # John pays $1000 per episode for the first half of the season
    cost_second_half = 1.2 * 1000 * (episodes // 2)  # The second half of the season is 120% more expensive
    total_cost = cost_first_half + cost_second_half  # Calculate the total cost of the season
    result = total_cost
    return result

print(solution())