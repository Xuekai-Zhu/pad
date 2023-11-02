def solution():
    # Calculate Barbara's current age
    barbara_age = 16 / 2

    # Calculate the age difference between Mike and Barbara
    age_diff = 16 - barbara_age

    # Calculate how many years until Mike is 24
    years_until_mike_24 = 24 - 16

    # Calculate how much Barbara will age during that time
    barbara_age_in_years_until_mike_24 = age_diff + years_until_mike_24

    # Calculate Barbara's age when Mike is 24
    barbara_age_when_mike_24 = barbara_age + barbara_age_in_years_until_mike_24

    result = barbara_age_when_mike_24
    return result

print(solution())