def solution():
    # Find the total number of parts in the ratio
    total_parts = 10 + 17

    # Find the number of parts representing last year's selfies
    last_year_parts = 10

    # Calculate the number of photos Malachi took last year
    last_year_photos = (last_year_parts / total_parts) * 2430

    # Calculate the number of photos Malachi took this year
    this_year_photos = 2430 - last_year_photos

    # Calculate the difference between the number of photos Malachi took this year and last year
    difference = this_year_photos - last_year_photos
    result = difference
    return result

print(solution())