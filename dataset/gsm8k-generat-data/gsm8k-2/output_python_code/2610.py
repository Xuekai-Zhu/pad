def solution():
    """Trevor is currently 11 years old and his older brother is 20 years old. How old will Trevor be when his older brother is three times as old as Trevor is now?"""
    trevor_age = 11
    brother_age = 20
    age_difference = brother_age - trevor_age

    # The age difference needs to triple, so divide by 2 and then multiply by 3
    triple_difference = age_difference / 2 * 3
    future_age = triple_difference + trevor_age
    result = future_age
    return result

print(solution())