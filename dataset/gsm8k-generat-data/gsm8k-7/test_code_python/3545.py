def solution():
    num_biscuits_per_day = 4
    biscuit_price = 0.25

    num_bones_per_day = 2
    bone_price = 1

    num_days = 7

    # Calculate the total number of biscuits that Belle will eat in a week
    total_biscuits = num_biscuits_per_day * num_days

    # Calculate the total number of bones that Belle will eat in a week
    total_bones= num_bones_per_day * num_days

    # Calculate the total cost of all biscuits and bones that Belle will eat in a week
    total_cost = (total_biscuits * biscuit_price) + (total_bones * bone_price)
    result = total_cost
    return result

print(solution())