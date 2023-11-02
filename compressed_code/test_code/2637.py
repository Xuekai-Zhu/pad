def solution():
    
    us_size = 1
    canada_size = 1.5 * us_size
    russia_size = (1 + (1/3)) * canada_size
    russia_to_us_ratio = russia_size / us_size
    result = russia_to_us_ratio
    return result

print(solution())