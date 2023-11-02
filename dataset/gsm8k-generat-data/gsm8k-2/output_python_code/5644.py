def solution():
    """If 12 bags of oranges weigh 24 pounds, how much do 8 bags weigh?"""
    bags = 12
    weight = 24
    weight_per_bag = weight / bags
    result = weight_per_bag * 8
    return result

print(solution())