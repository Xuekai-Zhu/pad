def solution():
    """James writes a 3-page letter to 2 different friends twice a week. How many pages does he write a year?"""
    # Define the number of pages in a letter and the frequency of letters
    PAGES_PER_LETTER = 3
    LETTERS_PER_WEEK = 2

    # Calculate the number of pages written per week
    pages_per_week = PAGES_PER_LETTER * LETTERS_PER_WEEK * 2

    # Calculate the number of pages written per year
    pages_per_year = pages_per_week * 52

    result = pages_per_year
    return result

print(solution())