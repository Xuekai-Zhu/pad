def solution():
    current_year = 2021
    mark_birth_year = 1976
    graham_age_difference = 3

    # Calculate the age of Mark in years
    mark_age = current_year - mark_birth_year

    # Calculate the age of Graham in years
    graham_age = mark_age - graham_age_difference

    # Calculate the age of Janice in years
    janice_age = graham_age / 2

    result = janice_age
    return result

print(solution())