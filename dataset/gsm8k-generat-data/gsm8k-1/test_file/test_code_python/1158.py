def solution():
    """Geb is 10 less than half the age of Haley. If Haley is 26 years old, how old is Geb?"""
    haley_age = 26
    half_haley_age = haley_age / 2
    geb_age = half_haley_age - 10
    result = geb_age
    return result

print(solution())