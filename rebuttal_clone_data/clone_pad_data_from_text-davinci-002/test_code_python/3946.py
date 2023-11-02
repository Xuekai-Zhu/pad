def solution():
    brownies_made = 2
    brownies_eaten = 8
    brownies_remaining = brownies_made - brownies_eaten
    new_brownies_made = 2
    total_brownies = brownies_remaining + new_brownies_made
    result = total_brownies
    return result

print(solution())