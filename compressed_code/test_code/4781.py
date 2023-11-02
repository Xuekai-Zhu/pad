def solution():
    
    total_brownies = 16
    children_brownies = total_brownies * 0.25
    remaining_brownies = total_brownies - children_brownies
    family_brownies = remaining_brownies * 0.5
    remaining_brownies -= family_brownies
    lorraine_brownies = remaining_brownies - 1
    result = lorraine_brownies
    return result

print(solution())