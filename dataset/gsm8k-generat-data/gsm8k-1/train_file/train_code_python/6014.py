def solution():
    """3 years ago James turned 27. In 5 years Matt will be twice James age. How old is Matt now?"""
    james_age_3_years_ago = 27 - 3
    matt_age_in_5_years = 2 * (james_age_3_years_ago + 5)
    matt_age = matt_age_in_5_years - 5
    result = matt_age
    return result

print(solution())