def solution():
    # Define the number of dog biscuits and rawhide bones eaten per day
    biscuits_per_day = 4
    bones_per_day = 2
    # Define the cost per dog biscuit and per rawhide bone
    biscuit_cost = 0.25
    bone_cost = 1

    # Calculate the daily cost of the treats
    daily_cost = (biscuits_per_day * biscuit_cost) + (bones_per_day * bone_cost)

    # Calculate the weekly cost of the treats
    weekly_cost = daily_cost * 7
    result = weekly_cost
    return result

print(solution())