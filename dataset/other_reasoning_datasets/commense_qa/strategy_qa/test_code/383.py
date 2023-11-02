def solution():
    gauss_birth_year = 1777
    telephone_invention_year = 1876
    gauss_age_at_invention = telephone_invention_year - gauss_birth_year
    if gauss_age_at_invention >= 100:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())