def solution():
    """School coaches bought sports equipment. Coach A bought ten new basketballs for $29 each, while coach B bought 14 new baseballs for $2.50 each and a baseball bat for $18. How much more did coach A spend than coach B?"""
    # Calculate the total cost for coach A's purchase
    coach_a_cost = 10 * 29

    # Calculate the total cost for coach B's purchase
    coach_b_cost = 14 * 2.5 + 18

    # Calculate the difference in cost between the two purchases
    cost_diff = coach_a_cost - coach_b_cost

    result = cost_diff
    return result

print(solution())