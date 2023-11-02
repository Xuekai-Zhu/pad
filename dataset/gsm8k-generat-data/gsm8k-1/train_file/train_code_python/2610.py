def solution():
    """Trevor is currently 11 years old and his older brother is 20 years old. How old will Trevor be when his older brother is three times as old as Trevor is now?"""
    trevor_age = 11
    older_brother_age = 20
    age_difference = older_brother_age - trevor_age
    target_age_difference = age_difference * 2
    target_age = older_brother_age + target_age_difference
    trevor_target_age_difference = target_age - trevor_age
    trevor_target_age = trevor_age + trevor_target_age_difference
    result = trevor_target_age
    return result

print(solution())