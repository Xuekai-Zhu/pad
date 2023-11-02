def solution():
    alan_birth_year = 1936
    vietnam_war_years = range(1955, 1976)
    american_involvement_years = range(1965, 1974)
    alan_age_in_1965 = 1965 - alan_birth_year
    if alan_age_in_1965 >= 18 and 1965 in american_involvement_years:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())