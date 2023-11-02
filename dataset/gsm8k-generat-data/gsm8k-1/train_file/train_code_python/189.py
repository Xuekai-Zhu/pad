def solution():
    """Last year Dallas was 3 times the age of his sister Darcy. Darcy is twice as old as Dexter who is 8 right now. How old is Dallas now?"""
    dexter_age = 8
    darcy_age = dexter_age * 2
    dallas_darcy_ratio = 3
    dallas_last_year = dallas_darcy_ratio * (darcy_age - 1)
    dallas_age = dallas_last_year + 1
    result = dallas_age
    return result

print(solution())