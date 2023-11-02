def solution():
    """Marianne was 20 years old when Bella was 8 years old. How old will Marianne be when Bella turns 18?"""
    # Define the age difference between Marianne and Bella
    age_difference = 20 - 8

    # Calculate the age at which Bella will turn 18
    bella_turns_18 = 18 + age_difference

    # Calculate Marianne's age at the time Bella turns 18
    marianne_age = bella_turns_18 + age_difference

    # Return the result
    result = marianne_age
    return result

print(solution())