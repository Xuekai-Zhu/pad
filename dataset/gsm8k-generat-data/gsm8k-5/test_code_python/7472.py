def solution():
    anika_age_now = 30  # Anika is currently 30 years old
    maddie_age_now = (3/4) * anika_age_now  # Maddie is 4/3 the age of Anika
    anika_age_in_15_years = anika_age_now + 15  # Anika's age in 15 years
    maddie_age_in_15_years = maddie_age_now + 15  # Maddie's age in 15 years

    # Calculate the average age of Anika and Maddie in 15 years
    average_age_in_15_years = (anika_age_in_15_years + maddie_age_in_15_years) / 2
    result = average_age_in_15_years
    return result

print(solution())