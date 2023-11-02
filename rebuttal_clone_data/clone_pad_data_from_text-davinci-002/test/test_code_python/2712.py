def solution():
    people_this_year = 600
    people_next_year = people_this_year * 2
    people_last_year = people_next_year - 200
    result = people_this_year + people_next_year + people_last_year
    return result

print(solution())