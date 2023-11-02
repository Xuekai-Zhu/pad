def solution():
    pages_per_letter = 3
    num_friends = 2
    num_weeks = 52
    letters_per_week = 2

    # Calculate the total number of letters James writes in a year
    total_letters = num_friends * num_weeks * letters_per_week

    # Calculate the total number of pages James writes in a year
    total_pages = total_letters * pages_per_letter
    result = total_pages
    return result

print(solution())