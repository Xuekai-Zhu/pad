def solution():
    """Duncan's age eight years ago was two times Adam's age four years ago. If Duncan's age is 60 now, how old will Adam be in 8 years?"""
    duncan_current_age = 60
    duncan_age_eight_years_ago = duncan_current_age - 8
    adam_age_four_years_ago = (duncan_age_eight_years_ago / 2) - 4
    adam_age_in_eight_years = adam_age_four_years_ago + 8
    result = adam_age_in_eight_years
    return result

print(solution())