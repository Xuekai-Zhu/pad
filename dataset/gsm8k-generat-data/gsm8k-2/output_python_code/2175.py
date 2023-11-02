def solution():
    """Maiya has two sisters. The first sister is twice as old as Maiya. The first sister is 1 year younger than Maiya. Their average age is 5. How old is Maiya?"""
    total_age = 15  # Their total age is 3 sisters * 5 years each
    first_sister_age = (total_age / 3) * 2 - 1  # First sister is twice Maiya's age and 1 year younger
    maiya_age = total_age / 3 - 1  # First sister is 1 year younger than Maiya
    result = maiya_age
    return result

print(solution())