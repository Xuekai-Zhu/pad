def solution():
    """3 years ago James turned 27. In 5 years Matt will be twice James age. How old is Matt now?"""
    james_age_3_years_ago = 27 - 3
    james_age_in_5_years = james_age_3_years_ago + 8  # 3 years ago + 5 years in the future
    matt_age_in_5_years = 2 * james_age_in_5_years
    matt_current_age = matt_age_in_5_years - 5  # subtracting 5 years for future age back to current age
    result = matt_current_age
    return result

print(solution())