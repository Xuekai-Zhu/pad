def solution():
    """Belle eats 4 dog biscuits and 2 rawhide bones every evening. If each rawhide bone is $1, and each dog biscuit is $0.25, then how much does it cost, in dollars, to feed Belle these treats for a week?"""
    biscuits_per_day = 4
    bones_per_day = 2
    cost_per_biscuit = 0.25
    cost_per_bone = 1
    days_per_week = 7
    total_cost = (biscuits_per_day * cost_per_biscuit + bones_per_day * cost_per_bone) * days_per_week
    result = total_cost
    return result

print(solution())