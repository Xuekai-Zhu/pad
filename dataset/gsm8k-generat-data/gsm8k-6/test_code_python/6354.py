def solution():
    sister_age = 13 + 6  # Nick's sister is 6 years older than him
    combined_age = 13 + sister_age  # combined age of Nick and his sister
    brother_age = combined_age / 2  # brother's age is half their combined age
    age_in_5_years = brother_age + 5  # brother's age in 5 years

    result = age_in_5_years
    return result

print(solution())