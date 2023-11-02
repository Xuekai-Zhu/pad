def solution():
    """James writes a 3-page letter to 2 different friends twice a week. How many pages does he write a year?"""
    # Define the number of letters James writes per week
    letters_per_week = 2 * 2

    # Define the number of pages James writes per letter
    pages_per_letter = 3

    # Calculate the number of pages James writes per week
    pages_per_week = letters_per_week * pages_per_letter

    # Calculate the number of pages James writes per year
    pages_per_year = pages_per_week * 52

    # return the result
    result = pages_per_year
    return result

print(solution())