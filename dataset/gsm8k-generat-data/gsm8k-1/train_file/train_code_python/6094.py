def solution():
    """Beau’s sons are triplets. They are 16 years old today. Three years ago, the sum of his 3 sons’ ages equaled Beau’s age. How old is Beau today?"""
    sons_age = 16
    total_age_3_years_ago = (sons_age - 3) * 3
    beau_age_3_years_ago = total_age_3_years_ago
    beau_age = beau_age_3_years_ago + 3 * 3
    result = beau_age
    return result

print(solution())