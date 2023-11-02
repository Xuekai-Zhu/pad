def solution():
    """Andy walks 50 meters from his house to school. After school, he comes back to the house and goes to the market. If he walks 140 meters in total, how many meters is the distance between the house and the market?"""
    distance_to_school = 50
    total_distance = 140
    distance_to_market = (total_distance - (2 * distance_to_school))
    result = distance_to_market
    return result

print(solution())