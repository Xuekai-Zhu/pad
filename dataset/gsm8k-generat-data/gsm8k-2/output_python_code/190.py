def solution():
    """Last year Dallas was 3 times the age of his sister Darcy. Darcy is twice as old as Dexter who is 8 right now. How old is Dallas now?"""
    dexter_age = 8
    darcy_age = 2 * dexter_age
    dallas_age_last_year = 3 * darcy_age
    dallas_age_now = dallas_age_last_year + 1  # Adding 1 for the year that passed
    result = dallas_age_now
    return result

print(solution())