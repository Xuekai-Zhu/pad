def solution():
    linkedin_launch_year = 2003
    kim_ilsung_death_year = 1994
    if kim_ilsung_death_year < linkedin_launch_year:
        result = "no"
    else:
        result = "unclear"
    return result

print(solution())