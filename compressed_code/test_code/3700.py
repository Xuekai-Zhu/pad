def solution():
    
    current_year = 600
    next_year = 2 * current_year
    last_year = next_year - 200
    total = current_year + next_year + last_year
    result = total
    return result

print(solution())