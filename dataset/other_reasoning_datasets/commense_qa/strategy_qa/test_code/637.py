def solution():
    average_doctorate_age = 33
    average_doctorate_years = 8.5
    claimed_doctorate_age = 21
    expected_years_of_study = claimed_doctorate_age - average_doctorate_age
    if expected_years_of_study >= average_doctorate_years:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())