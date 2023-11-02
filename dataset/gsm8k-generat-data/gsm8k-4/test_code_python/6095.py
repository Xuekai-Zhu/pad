def solution():
    """Beau’s sons are triplets. They are 16 years old today. Three years ago, the sum of his 3 sons’ ages equaled Beau’s age. How old is Beau today?"""
    # Define the current age of the triplets
    triplets_age = 16

    # Calculate the sum of their ages three years ago
    sum_three_years_ago = (triplets_age - 3) * 3

    # Calculate Beau's age three years ago
    beau_three_years_ago = sum_three_years_ago

    # Calculate Beau's current age
    beau_age = beau_three_years_ago + 3*3

    # return the result
    result = beau_age
    return result

print(solution())