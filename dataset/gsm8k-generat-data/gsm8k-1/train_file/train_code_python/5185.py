def solution():
    """8 years ago James was twice Janet's age. In 15 years James will turn 37. Susan was born when Janet turned 3. How old will Susan turn in 5 years?"""
    james_in_15_years = 37
    janet_in_15_years = james_in_15_years - 8 * 2
    susan_age_difference = janet_in_15_years - 3
    susan_age = 15 + susan_age_difference
    susan_age_in_5_years = susan_age + 5
    result = susan_age_in_5_years
    return result

print(solution())