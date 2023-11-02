def solution():
    older_brother_birth_year = 1932
    older_sister_birth_year = 1936

    # Calculate the gap between the older brother and sister
    gap_brother_sister = older_sister_birth_year - older_brother_birth_year

    # Calculate the gap between the grandmother and sister
    gap_grandmother_sister = gap_brother_sister * 2

    # Calculate the grandmother's birth year
    grandmother_birth_year = older_sister_birth_year + gap_grandmother_sister
    result = grandmother_birth_year
    return result

print(solution())