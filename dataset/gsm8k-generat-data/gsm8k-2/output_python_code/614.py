def solution():
    """Connie is trying to remember when her grandmother was born. She knows her grandmother's older brother was born in 1932, her older sister was born in 1936, and the gap between her grandmother and her sister is twice the gap between the older brother and the older sister. What year was Connie's grandma born?"""
    older_brother_birth_year = 1932
    older_sister_birth_year = 1936
    sister_brother_gap = older_sister_birth_year - older_brother_birth_year
    grandma_sister_gap = 2 * sister_brother_gap
    sister_birth_year = older_sister_birth_year + sister_brother_gap
    grandma_birth_year = sister_birth_year - grandma_sister_gap
    result = grandma_birth_year
    return result

print(solution())