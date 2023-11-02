def solution():
    older_brother_year = 1932
    older_sister_year = 1936

    # Calculate the gap between the older brother and older sister
    bro_sis_gap = older_sister_year - older_brother_year

    # Calculate the gap between the grandmother and older sister
    grandma_sis_gap = bro_sis_gap * 2

    # Calculate the year of Connie's grandmother's birth
    grandma_year = older_sister_year + grandma_sis_gap
    result = grandma_year
    return result

print(solution())