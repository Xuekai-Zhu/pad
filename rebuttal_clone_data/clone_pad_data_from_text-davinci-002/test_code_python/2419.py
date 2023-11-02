def solution():
    total_meat_needed = 210
    cubs_meat_needed = 4 * 35
    bear_meat_needed = total_meat_needed - cubs_meat_needed
    rabbit_weight = 5
    rabbits_needed = (bear_meat_needed / rabbit_weight) + (cubs_meat_needed / rabbit_weight)
    result = rabbits_needed
    return result

print(solution())