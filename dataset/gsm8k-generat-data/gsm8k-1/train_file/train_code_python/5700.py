def solution():
    """Alvin is 30 years old and Simon is 5 years away from being 1/2 the age of Alvin. How old is Simon?"""
    alvin_age = 30
    simon_half_age = alvin_age/2 - 5
    simon_age = simon_half_age * 2
    result = simon_age
    return result

print(solution())