def solution():
    """Last year Dallas was 3 times the age of his sister Darcy. Darcy is twice as old as Dexter who is 8 right now. How old is Dallas now?"""
    darcy_age_last_year = 8 / 2
    dallas_age_last_year = darcy_age_last_year * 3
    dallas_age_now = dallas_age_last_year + 1
    result = dallas_age_now 
    return result

print(solution())