def solution():
    """Milena is 7 years old, and her grandmother is 9 times older than her. Milena's grandfather is two years older than her grandmother. What is the age difference between Milena and her grandfather?"""
    # Calculate the age of Milena's grandmother
    grandmother_age = 7 * 9

    # Calculate the age of Milena's grandfather
    grandfather_age = grandmother_age + 2

    # Calculate the age difference between Milena and her grandfather
    age_difference = grandfather_age - 7

    result = age_difference
    return result

print(solution())