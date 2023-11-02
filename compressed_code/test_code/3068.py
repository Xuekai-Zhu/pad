def solution():
    
    initial_brownies = 2 * 12
    eaten_brownies = 8 + 4
    remaining_brownies = initial_brownies - eaten_brownies
    total_brownies = remaining_brownies + 2 * 12
    result = total_brownies
    return result

print(solution())