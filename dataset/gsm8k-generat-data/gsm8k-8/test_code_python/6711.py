def solution():
    # Define Sierra's age
    sierra_age = 30

    # Calculate 10 times Sierra's age plus 20
    ten_sierra_age_plus_20 = 10 * sierra_age + 20

    # Calculate 40 less than 10 times Diaz's age
    forty_less_than_10_diaz_age = ten_sierra_age_plus_20 - 40

    # Solve for Diaz's age
    ten_diaz_age = forty_less_than_10_diaz_age + 40
    diaz_age = ten_diaz_age / 10

    # Calculate Diaz's age 20 years from now
    diaz_age_in_20_years = diaz_age + 20

    result = diaz_age_in_20_years
    return result

print(solution())