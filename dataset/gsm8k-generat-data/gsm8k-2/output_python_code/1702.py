def solution():
    """School coaches bought sports equipment. Coach A bought ten new basketballs for $29 each, while coach B bought 14 new baseballs for $2.50 each and a baseball bat for $18. How much more did coach A spend than coach B?"""
    coach_a_spent = 10 * 29
    coach_b_spent = 14 * 2.5 + 18
    difference = coach_a_spent - coach_b_spent
    result = difference
    return result

print(solution())