def solution():
    ratio = 10 / 17  # Ratio of photos taken last year to photos taken this year
    total_photos = 2430  # Total number of photos in Malachi's gallery

    # Calculate the number of photos taken last year and this year
    last_year_photos = (ratio / (1 + ratio)) * total_photos
    this_year_photos = (1 / (1 + ratio)) * total_photos

    # Calculate the difference in the number of photos taken this year and last year
    difference = this_year_photos - last_year_photos
    result = difference
    return result

print(solution())