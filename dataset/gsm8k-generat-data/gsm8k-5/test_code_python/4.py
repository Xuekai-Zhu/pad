def solution():
    pages_per_letter = 3  # James writes a 3-page letter to each friend
    friends = 2  # James has 2 friends he writes to
    letters_per_week = 2  # James writes 2 letters per week
    weeks_per_year = 52  # There are 52 weeks in a year

    # Calculate the total number of pages James writes in a year
    total_pages = pages_per_letter * friends * letters_per_week * weeks_per_year
    result = total_pages
    return result

print(solution())