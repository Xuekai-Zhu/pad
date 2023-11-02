def solution():
    """8 years ago James was twice Janet's age. In 15 years James will turn 37. Susan was born when Janet turned 3. How old will Susan turn in 5 years?"""
    james_age_in_8_years = 37 - 15 - 8
    janet_age_in_8_years = james_age_in_8_years / 2
    janet_age_now = janet_age_in_8_years + 8
    susan_age_now = 3 + janet_age_now
    susan_age_in_5_years = susan_age_now + 5
    result = susan_age_in_5_years
    return result

print(solution())