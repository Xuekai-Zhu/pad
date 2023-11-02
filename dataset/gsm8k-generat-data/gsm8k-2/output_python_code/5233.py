def solution():
    """Milena is 7 years old, and her grandmother is 9 times older than her. Milena's grandfather is two years older than her grandmother. What is the age difference between Milena and her grandfather?"""
    milena_age = 7
    grandmother_age = 9 * milena_age
    grandfather_age = grandmother_age + 2
    age_difference = grandfather_age - milena_age
    result = age_difference
    return result

print(solution())