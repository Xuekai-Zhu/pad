def solution():
    # Find Tully's age three years from now
    tully_future_age = 2 * (29 + 3)  
    # Find Tully's current age
    tully_current_age = tully_future_age - 3  
    # Find Tully's age a year ago
    tully_age_1_year_ago = tully_current_age - 1

    result = tully_age_1_year_ago
    return result

print(solution())