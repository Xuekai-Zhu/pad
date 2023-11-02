def solution():
    """Tommy is making steaks for his family. There are 5 of them in total. If each member wants one pound and the steaks are 20 ounces each, how many does he need to buy?"""
    num_people = 5
    oz_per_lb = 16
    oz_per_steak = 20
    lbs_needed = num_people * oz_per_lb / oz_per_steak
    result = lbs_needed
    return result

print(solution())