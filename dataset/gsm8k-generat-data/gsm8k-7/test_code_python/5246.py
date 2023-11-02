def solution():
    dog1_min = 10
    dog2_min = 7
    dog3_min = 9
    dog1_cost = 20 + dog1_min
    dog2_cost = 2 * (20 + dog2_min)
    dog3_cost = 3 * (20 + dog3_min)
    total_cost = dog1_cost + dog2_cost + dog3_cost
    result = total_cost
    return result

print(solution())