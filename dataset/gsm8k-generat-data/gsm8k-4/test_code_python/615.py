def solution():
    """Connie is trying to remember when her grandmother was born. She knows her grandmother's older brother was born in 1932, her older sister was born in 1936, and the gap between her grandmother and her sister is twice the gap between the older brother and the older sister. What year was Connie's grandma born?"""
    # Define the birth year of the older brother and older sister
    brother_birth_year = 1932
    sister_birth_year = 1936

    # Calculate the gap between the older brother and older sister
    brother_sister_gap = sister_birth_year - brother_birth_year

    # Calculate the gap between the grandmother and her sister
    grandmother_sister_gap = 2 * brother_sister_gap

    # Calculate the birth year of the grandmother
    grandmother_birth_year = sister_birth_year + grandmother_sister_gap

    result = grandmother_birth_year
    return result

print(solution())