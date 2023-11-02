def solution():
    """In his phone gallery, Malachi has the number of selfies he took last year and this year in the ratio of 10:17. If he has 2430 photos in his gallery, how many more photos did he take this year than last year?"""
    # Define the ratio of photos taken last year to this year
    ratio_last_to_this = 10 / 17

    # Calculate the total number of photos
    total_photos = 2430

    # Calculate the number of photos taken last year
    last_year_photos = total_photos / (1 + ratio_last_to_this)

    # Calculate the number of photos taken this year
    this_year_photos = last_year_photos * ratio_last_to_this

    # Calculate the difference in the number of photos taken this year and last year
    difference = this_year_photos - last_year_photos

    # Display the difference
    result = difference
    return result

print(solution())