def solution():
    """In 10 years, Cornelia will be three times as old as Kilee. If Kilee is currently 20 years old, how old is Cornelia now?"""
    kilee_age_now = 20
    cornelia_age_in_10_years = 3 * (kilee_age_now + 10)
    cornelia_age_now = cornelia_age_in_10_years - 10
    result = cornelia_age_now
    return result

print(solution())