def solution():
    """If I'm 4 times older than Billy currently, and Billy is 4 years old, how old was I when Billy was born?"""
    billy_age = 4
    my_age = 4 * billy_age
    age_difference = my_age - billy_age
    my_age_when_billy_was_born = age_difference - billy_age
    result = my_age_when_billy_was_born
    return result

print(solution())