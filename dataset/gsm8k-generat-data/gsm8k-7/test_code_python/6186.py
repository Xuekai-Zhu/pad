def solution():
    tom_current_age = 37  # Tom turned 32, 5 years ago
    jim_age_7_years_ago = (tom_current_age / 2) - 5 + 5  # Jim was 5 years older than half of Tom's age, 7 years ago
    jim_current_age = jim_age_7_years_ago + 7  # Add 7 years to Jim's age to get his current age
    jim_age_in_2_years = jim_current_age + 2  # Add 2 years to Jim's current age to get his age in 2 years
    result = jim_age_in_2_years
    return result

print(solution())