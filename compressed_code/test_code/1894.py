def solution():
    
    total_brownies = 20
    lounge_brownies = total_brownies // 2
    remaining_brownies = total_brownies - lounge_brownies
    carl_brownies = remaining_brownies // 2
    simon_brownies = 2
    left_brownies = remaining_brownies - carl_brownies - simon_brownies
    result = left_brownies
    return result

print(solution())