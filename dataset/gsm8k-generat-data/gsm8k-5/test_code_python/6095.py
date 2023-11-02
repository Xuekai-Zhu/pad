def solution():
    sons_current_age = 16  # Beau's sons are currently 16 years old
    sum_sons_ages_3_years_ago = (sons_current_age * 3) - 9  # Three years ago, the sum of his sons' ages equaled Beau's age
    beau_age_3_years_ago = sum_sons_ages_3_years_ago  # Beau's age three years ago was equal to the sum of his sons' ages three years ago
    beau_current_age = beau_age_3_years_ago + 3*3  # Add 3 years to each age (one year for each of the past 3 years) to find the current age
    result = beau_current_age
    return result

print(solution())