def solution():
    """Maiya has two sisters. The first sister is twice as old as Maiya. The first sister is 1 year younger than Maiya. Their average age is 5. How old is Maiya?"""
    first_sister_age = 2 * x
    maiya_age = x + 1
    total_age = first_sister_age + maiya_age + x
    average_age = total_age / 3
    average_age = 5
    x = (average_age * 3) - (maiya_age + first_sister_age)
    result = maiya_age
    return result

print(solution())