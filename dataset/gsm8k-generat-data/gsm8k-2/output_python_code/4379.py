def solution():
    """In his phone gallery, Malachi has the number of selfies he took last year and this year in the ratio of 10:17. If he has 2430 photos in his gallery, how many more photos did he take this year than last year?"""
    ratio = 10/17
    total = 2430
    last_year_photos = total / (ratio + 1)
    this_year_photos = total - last_year_photos
    difference = this_year_photos - last_year_photos
    result = difference
    return result

print(solution())