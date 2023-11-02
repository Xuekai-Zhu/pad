def solution():
    current_age = 16
    years_ago = 3

    # Calculate the sum of Beau's sons' ages three years ago
    sum_ages_3_years_ago = (current_age - years_ago) * 3

    # Calculate Beau's age three years ago
    beau_age_3_years_ago = sum_ages_3_years_ago

    # Calculate Beau's current age
    beau_current_age = beau_age_3_years_ago + years_ago * 3
    result = beau_current_age
    return result

print(solution())