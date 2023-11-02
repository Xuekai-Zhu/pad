def solution():
    
    beef_weight = 10
    noodle_weight_ratio = 2
    noodle_weight = beef_weight * noodle_weight_ratio
    already_have_noodles = 4
    remaining_noodles_needed = noodle_weight - already_have_noodles
    packages_needed = (remaining_noodles_needed + 1) // 2 
    result = packages_needed
    return result

print(solution())