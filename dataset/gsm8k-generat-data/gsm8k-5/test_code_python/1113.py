def solution():
    younger_brother_age = 10  # Viggo's younger brother is currently 10 years old
    brother_age_when_viggo_was_2_years_old = younger_brother_age - 2  # This is when Viggo's age was 10 more than twice his brother's age
    viggo_age_when_brother_was_2 = (brother_age_when_viggo_was_2_years_old - 10) / 2  # Calculate Viggo's age when his brother was 2

    # Calculate the current ages of Viggo and his brother
    viggo_age = viggo_age_when_brother_was_2 + 12  # Viggo aged 2 more years since his brother was 2
    brother_age = younger_brother_age

    # Calculate the sum of their ages
    total_age = viggo_age + brother_age
    result = total_age
    return result

print(solution())