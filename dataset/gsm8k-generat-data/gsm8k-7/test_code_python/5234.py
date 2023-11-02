def solution():
    milena_age = 7
    grandmother_age = 9 * milena_age
    grandfather_age = grandmother_age + 2

    # Calculate the age difference between Milena and her grandfather
    age_difference = grandfather_age - milena_age
    result = age_difference
    return result

print(solution())