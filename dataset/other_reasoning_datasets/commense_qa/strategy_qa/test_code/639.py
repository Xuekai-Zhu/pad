def solution():
    birth_year = 1942
    second_child_year = 1957
    voting_age = 18
    if birth_year + voting_age <= second_child_year:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())