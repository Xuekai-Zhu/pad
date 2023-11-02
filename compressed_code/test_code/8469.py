def solution():
    
    tomas_fudge = 1.5
    katya_fudge = 0.5
    boris_fudge = 2
    total_fudge = tomas_fudge + katya_fudge + boris_fudge
    ounces_per_pound = 16
    total_ounces = total_fudge * ounces_per_pound
    result = total_ounces
    return result

print(solution())