def solution():
    # Calculate Jessica's mother's age when she died
    mother_age_at_death = 70 - 10  # If her mother were alive now, ten years later, she would have been 70
    # Calculate Jessica's age at the time of her mother's death
    jessica_age_at_death = mother_age_at_death / 2
    # Calculate Jessica's current age
    jessica_current_age = jessica_age_at_death + 10  # adding 10 years
    result = jessica_current_age
    return result

print(solution())