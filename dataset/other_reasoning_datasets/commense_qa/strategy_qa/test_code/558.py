def solution():
    # Define that actuaries go through rigorous mathematics studies
    actuaries_rigorous_mathematical_training = True
    # Define that prime numbers are introduced in basic high school mathematics
    prime_numbers_introduced_in_high_school = True
    # Check if an actuary would be confused about prime numbers
    if actuaries_rigorous_mathematical_training and prime_numbers_introduced_in_high_school:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())