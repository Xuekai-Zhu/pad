def solution():
    
    # Define Duncan's current age and calculate Adam's age 8 years ago
    duncan_age = 60
    adam_age_8_years_ago = (duncan_age - 8) / 2

    # Calculate Adam's current age
    adam_age = adam_age_8_years_ago + 4

    # Calculate Adam's age in 8 years
    adam_age_in_8_years = adam_age + 8

    # Display Adam's age in 8 years
    result = adam_age_in_8_years
    return result

print(solution())