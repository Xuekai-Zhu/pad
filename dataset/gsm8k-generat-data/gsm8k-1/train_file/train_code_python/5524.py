def solution():
    """Abie had 20 bags of chips. She gave 4 bags to her friend and bought another 6 bags of chips in the store. How many bags of chips does Abie have in the end?"""
    initial_bags = 20
    bags_given = 4
    bags_bought = 6
    total_bags = initial_bags - bags_given + bags_bought
    result = total_bags
    return result

print(solution())