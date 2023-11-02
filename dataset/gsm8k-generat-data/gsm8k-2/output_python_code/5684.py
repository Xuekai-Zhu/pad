def solution():
    """In 10 years, Cornelia will be three times as old as Kilee. If Kilee is currently 20 years old, how old is Cornelia now?"""
    kilee_age = 20
    cornelia_age_in_10_years = 3 * (kilee_age + 10)
    cornelia_age = cornelia_age_in_10_years - 10
    result = cornelia_age
    return result

print(solution())