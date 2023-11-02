def solution():
    # Calculate the age gap between the brother and sister
    gap_brother_sister = 1936 - 1932  

    # Calculate the age gap between the sister and grandmother
    gap_sister_grandmother = gap_brother_sister * 2 

    # Calculate the birth year of the grandmother
    birth_year_grandmother = 1936 + gap_sister_grandmother  

    result = birth_year_grandmother
    return result

print(solution())