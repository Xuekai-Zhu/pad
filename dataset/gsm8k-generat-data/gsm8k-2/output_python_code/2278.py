def solution():
    """Austin has 10 pairs of dress shoes he needs to polish over the weekend. If he has polished 45% of individual shoes, how many more shoes does he need to polish?"""
    total_shoes = 10*2 # 10 pairs of shoes, each pair has 2 individual shoes
    polished_shoes = int(total_shoes * 0.45) # 45% of individual shoes
    unpolished_shoes = total_shoes - polished_shoes
    result = unpolished_shoes
    return result

print(solution())