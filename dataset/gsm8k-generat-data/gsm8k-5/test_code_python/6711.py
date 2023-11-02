def solution():
    sierra_age = 30  # Sierra is currently 30 years old
    diaz_equation = 10 * diaz_age - 40  # The equation for Diaz's age
    sierra_equation = 10 * sierra_age + 20  # The equation for Sierra's age

    # Solve for Diaz's age using the two equations
    diaz_age = (sierra_equation + 40) / 10

    # Calculate Diaz's age 20 years from now
    diaz_age_20_years = diaz_age + 20
    result = diaz_age_20_years
    return result

print(solution())