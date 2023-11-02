def solution():
    # Define the number of letters James writes per week
    letters_per_week = 2 * 2

    # Define the number of pages James writes per letter
    pages_per_letter = 3

    # Calculate the number of pages James writes per week
    pages_per_week = letters_per_week * pages_per_letter

    # Calculate the number of pages James writes per year (assuming 52 weeks per year)
    pages_per_year = pages_per_week * 52

    result = pages_per_year
    return result

print(solution())