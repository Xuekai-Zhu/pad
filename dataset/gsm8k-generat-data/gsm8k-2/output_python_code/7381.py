def solution():
    """Tommy is making steaks for his family. There are 5 of them in total. If each member wants one pound and the steaks are 20 ounces each, how many does he need to buy?"""
    total_members = 5
    desired_weight = 16  # 1 pound = 16 ounces
    steak_weight = 20
    total_steaks = (total_members * desired_weight) / (steak_weight/16)  # converting steak_weight to pounds
    result = total_steaks
    return result

print(solution())