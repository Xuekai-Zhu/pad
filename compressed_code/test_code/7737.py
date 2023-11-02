def solution():
    
    starting_legos = 380
    lost_legos = 57
    given_legos = 24
    remaining_legos = starting_legos - lost_legos - given_legos
    result = remaining_legos
    return result

print(solution())