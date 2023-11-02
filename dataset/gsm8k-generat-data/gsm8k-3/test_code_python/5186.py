def solution():
    '''8 years ago James was twice Janet's age.
    In 15 years James will turn 37.
    Susan was born when Janet turned 3.
    How old will Susan turn in 5 years?'''

    # current age of James
    james_current_age = 37 - 15

    # age of James 8 years ago
    james_age_8_years_ago = james_current_age - 8

    # age of James when he was twice Janet's age
    janet_age_8_years_ago = james_age_8_years_ago / 2

    # current age of Janet
    janet_current_age = janet_age_8_years_ago + 8

    # age of Janet when Susan was born
    janet_age_when_susan_born = 3

    # current age of Susan
    current_year = 2022
    susan_current_age = current_year - (janet_age_when_susan_born + janet_current_age)

    # age of Susan in 5 years
    susan_age_in_5_years = susan_current_age + 5

    result = susan_age_in_5_years
    return result

print(solution())