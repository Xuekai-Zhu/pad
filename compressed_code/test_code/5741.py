def solution():
    
    ounce_per_cap = 1 / 7
    pound_per_ounce = 1 / 16
    total_ounces = 18 / pound_per_ounce
    total_caps = total_ounces / ounce_per_cap
    result = total_caps
    return result

print(solution())