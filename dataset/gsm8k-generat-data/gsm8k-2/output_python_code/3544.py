def solution():
    """Belle eats 4 dog biscuits and 2 rawhide bones every evening. If each rawhide bone is $1, and each dog biscuit is $0.25, then how much does it cost, in dollars, to feed Belle these treats for a week?"""
    biscuits_per_day = 4
    bones_per_day = 2
    biscuit_cost = 0.25
    bone_cost = 1

    cost_per_day = (biscuits_per_day * biscuit_cost) + (bones_per_day * bone_cost)
    cost_per_week = cost_per_day * 7

    result = cost_per_week
    return result

print(solution())