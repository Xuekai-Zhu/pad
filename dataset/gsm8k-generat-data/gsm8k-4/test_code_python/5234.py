def solution():
    """Milena is 7 years old, and her grandmother is 9 times older than her. Milena's grandfather is two years older than her grandmother. What is the age difference between Milena and her grandfather?"""
    # Define Milena's age
    milena_age = 7

    # Calculate the grandmother's age
    grandmother_age = milena_age * 9

    # Calculate the grandfather's age
    grandfather_age = grandmother_age + 2

    # Calculate the age difference between Milena and her grandfather
    age_difference = grandfather_age - milena_age

    # return the result
    result = age_difference
    return result

print(solution())