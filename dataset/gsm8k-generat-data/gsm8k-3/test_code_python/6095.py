def solution():
    """Beau’s sons are triplets.  They are 16 years old today.  Three years ago, the sum of his 3 sons’ ages equaled Beau’s age.  How old is Beau today?"""
    # Calculate the sum of Beau's sons' ages three years ago
    sons_age_sum = 3 * (16 - 3)

    # Calculate Beau's age three years ago
    beau_age_3_years_ago = sons_age_sum

    # Calculate Beau's current age
    beau_age = beau_age_3_years_ago + 3 * 3

    # Display Beau's current age
    result = beau_age
    return result

print(solution())