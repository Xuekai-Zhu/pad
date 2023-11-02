def solution():
    """Abie had 20 bags of chips. She gave 4 bags to her friend and bought another 6 bags of chips in the store. How many bags of chips does Abie have in the end?"""
    initial_bags = 20
    given_away_bags = 4
    bought_bags = 6
    remaining_bags = initial_bags - given_away_bags + bought_bags
    result = remaining_bags
    return result

print(solution())