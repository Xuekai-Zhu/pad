def solution():
    viking_era_end_year = 1066
    norman_survey_year = 1800
    if norman_survey_year > viking_era_end_year:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())