def solution():
    """If 12 bags of oranges weigh 24 pounds, how much do 8 bags weigh?"""
    bags1 = 12
    weight1 = 24
    bags2 = 8
    weight2 = (weight1/bags1)*bags2
    result = weight2
    return result

print(solution())