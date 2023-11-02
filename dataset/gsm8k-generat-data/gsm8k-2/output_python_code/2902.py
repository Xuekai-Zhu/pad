def solution():
    """Lexie is 6 years older than her brother and her sister is twice her age. If Lexie is 8, what is the age difference between her brother and her sister?"""
    lexie_age = 8
    brother_age = lexie_age - 6
    sister_age = 2 * lexie_age
    age_difference = sister_age - brother_age
    result = age_difference
    return result

print(solution())