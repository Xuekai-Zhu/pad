def solution():
    biscuits_per_day = 4  # Belle eats 4 dog biscuits per day
    bones_per_day = 2  # Belle eats 2 rawhide bones per day
    cost_per_bone = 1  # Each rawhide bone costs $1
    cost_per_biscuit = 0.25  # Each dog biscuit costs $0.25
    days_per_week = 7  # There are 7 days in a week

    # Calculate the total cost per day
    total_cost_per_day = (biscuits_per_day * cost_per_biscuit) + (bones_per_day * cost_per_bone)

    # Calculate the total cost for a week
    total_cost_per_week = total_cost_per_day * days_per_week
    result = total_cost_per_week
    return result

print(solution())