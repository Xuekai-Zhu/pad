def solution():
    # Define Marianne's current age and Bella's current age
    marianne_age = 20
    bella_age = 8

    # Calculate the age difference between Marianne and Bella
    age_difference = marianne_age - bella_age

    # Calculate the number of years until Bella turns 18
    years_until_bella_turns_18 = 18 - bella_age

    # Calculate Marianne's age when Bella turns 18
    marianne_age_when_bella_turns_18 = marianne_age + years_until_bella_turns_18

    result = marianne_age_when_bella_turns_18
    return result

print(solution())