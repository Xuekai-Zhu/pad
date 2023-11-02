def solution():
    age_difference = 4
    age_in_10_years = 40
    half_age_in_10_years = age_in_10_years / 2
    juanico_age_in_10_years = half_age_in_10_years - age_difference
    juanico_age_in_30_years = juanico_age_in_10_years + 20
    result = juanico_age_in_30_years
    return result

print(solution())