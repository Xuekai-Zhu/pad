def solution():
    """School coaches bought sports equipment. Coach A bought ten new basketballs for $29 each, while coach B bought 14 new baseballs for $2.50 each and a baseball bat for $18. How much more did coach A spend than coach B?"""
    cost_a = 10 * 29
    cost_b = (14 * 2.5) + 18
    difference = cost_a - cost_b
    result = difference
    return result

print(solution())