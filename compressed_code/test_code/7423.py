def solution():
    
    popsicles = 6
    melt_factor = 2
    remaining_popsicles = popsicles
    total_factor = 1
    while remaining_popsicles > 1:
        total_factor *= melt_factor
        remaining_popsicles -= 1
    result = total_factor
    return result

print(solution())