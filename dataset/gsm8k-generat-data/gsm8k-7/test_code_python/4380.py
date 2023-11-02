def solution():
    ratio = 10 / 17
    total_photos = 2430

    # Calculate the number of photos Malachi took last year
    last_year_photos = total_photos / (ratio + 1)

    # Calculate the number of photos Malachi took this year
    this_year_photos = last_year_photos * 17 / 10

    # Calculate the difference between the number of photos Malachi took this year and last year
    difference = this_year_photos - last_year_photos
    result = difference
    return result

print(solution())