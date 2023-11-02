def solution():
    
    this_year = 600
    next_year = 2 * this_year
    last_year = next_year - 200
    total_people = this_year + next_year + last_year
    result = total_people
    return result

print(solution())