def solution():
    leap_years = [1996, 2000, 2004, 2008, 2012, 2016, 2020]
    birth_year = 1996
    leap_years_since_birth = [year for year in leap_years if year > birth_year]
    leap_years_since_birth_count = len(leap_years_since_birth)
    # Since a leap year baby is technically born on February 29th, they only have a birthday every 4 years
    age_in_years = leap_years_since_birth_count // 4
    if age_in_years == 1:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())