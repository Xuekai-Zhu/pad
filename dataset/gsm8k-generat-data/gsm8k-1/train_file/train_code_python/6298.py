def solution():
    """Ariel began fencing in 2006. If she was born in 1992 and has been fencing for 16 years, how old is she now?"""
    start_year = 2006
    birth_year = 1992
    years_fencing = 16
    current_year = start_year + years_fencing
    age = current_year - birth_year
    result = age
    return result

print(solution())