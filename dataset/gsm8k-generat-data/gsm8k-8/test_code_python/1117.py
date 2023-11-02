def solution():
    # Gladys is 30 years old
    gladys_age = 30

    # Billy is 3 times younger than Gladys
    billy_age = gladys_age / 3

    # The sum of Billy's and Lucas's ages is half of Gladys's age
    sum_of_billy_and_lucas = gladys_age / 2 - billy_age

    # Lucas's current age
    lucas_age = sum_of_billy_and_lucas

    # Lucas's age in 3 years
    lucas_age_in_3_years = lucas_age + 3

    result = lucas_age_in_3_years
    return result

print(solution())