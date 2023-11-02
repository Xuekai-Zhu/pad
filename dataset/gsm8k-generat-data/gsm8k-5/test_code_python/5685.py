def solution():
    kilee_age_now = 20  # Kilee is currently 20 years old
    cornelia_age_in_10_years = 3 * (kilee_age_now + 10)  # Cornelia will be three times as old as Kilee in 10 years
    cornelia_age_now = cornelia_age_in_10_years - 10  # Subtracting 10 years to get Cornelia's current age

    result = cornelia_age_now
    return result

print(solution())