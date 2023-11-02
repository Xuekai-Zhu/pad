def solution():
    """Connie is trying to remember when her grandmother was born. She knows her grandmother's older brother was born in 1932, her older sister was born in 1936, and the gap between her grandmother and her sister is twice the gap between the older brother and the older sister. What year was Connie's grandma born?"""
    older_brother_birth_year = 1932
    older_sister_birth_year = 1936

    gap_between_brother_and_sister = older_sister_birth_year - older_brother_birth_year

    gap_between_grandma_and_sister = gap_between_brother_and_sister * 2

    grandma_birth_year = older_sister_birth_year - gap_between_grandma_and_sister

    result = grandma_birth_year
    return result

print(solution())