def solution():
    """Brenda picks 250 peaches. When she sorts through them, only 60% are fresh, and Brenda has to throw 15 away for being too small. How many peaches does Brenda have left?"""
    total_peaches = 250
    fresh_peaches = total_peaches * 0.6
    discarded_peaches = 15
    remaining_peaches = fresh_peaches - discarded_peaches
    result = remaining_peaches
    return result

print(solution())