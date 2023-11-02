def solution():
    """Marianne was 20 years old when Bella was 8 years old. How old will Marianne be when Bella turns 18?"""
    # Define the ages of Marianne and Bella
    marianne_age = 20
    bella_age = 8

    # Calculate the age difference between Marianne and Bella
    age_diff = marianne_age - bella_age

    # Calculate the age at which Bella turns 18
    bella_turns_18 = 18 + age_diff

    # Calculate Marianne's age when Bella turns 18
    marianne_turns_18 = marianne_age + bella_turns_18 - bella_age

    # Display Marianne's age when Bella turns 18
    result = marianne_turns_18
    return result

print(solution())