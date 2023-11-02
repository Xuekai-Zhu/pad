def solution():
    
    glasses = [2, 4] + [3]*4
    total_ounces = sum(glasses) * 10
    target_ounces = 220
    remaining_ounces = target_ounces - total_ounces
    saturday_glasses = remaining_ounces / 10
    result = saturday_glasses
    return result

print(solution())