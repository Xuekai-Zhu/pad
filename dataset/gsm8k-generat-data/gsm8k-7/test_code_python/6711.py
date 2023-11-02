def solution():
    sierra_age = 30
    diaz_equation = 10 * diaz_age - 40
    sierra_equation = 10 * sierra_age + 20

    # Solve for Diaz's age
    diaz_age = (sierra_equation + 40) / 10

    # Calculate Diaz's age 20 years from now
    diaz_age_20_years_from_now = diaz_age + 20
    result = diaz_age_20_years_from_now
    return result

print(solution())