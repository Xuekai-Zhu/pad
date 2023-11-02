def solution():
    num_biscuits = 4
    num_bones = 2
    price_biscuits = 0.25
    price_bones = 1
    cost_per_day = num_biscuits * price_biscuits + num_bones * price_bones
    cost_per_week = cost_per_day * 7
    result = cost_per_week
    return result

print(solution())