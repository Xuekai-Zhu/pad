def solution():
    older_brother_birth_year = 1932
    older_sister_birth_year = 1936
    gap = older_sister_birth_year - older_brother_birth_year
    grandmother_birth_year = older_sister_birth_year + (2 * gap)
    result = grandmother_birth_year
    return result

print(solution())