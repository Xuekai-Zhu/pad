def solution():
    
    total_brownies = 20
    admin_brownies = total_brownies / 2
    remaining_brownies = total_brownies - admin_brownies
    carl_brownies = remaining_brownies / 2
    remaining_brownies = remaining_brownies - carl_brownies - 2
    result = remaining_brownies
    return result

print(solution())