def solution():
    """In his phone gallery, Malachi has the number of selfies he took last year and this year in the ratio of 10:17. If he has 2430 photos in his gallery, how many more photos did he take this year than last year?"""
    ratio_last_year = 10
    ratio_this_year = 17
    total_ratio = ratio_last_year + ratio_this_year
    total_photos = 2430
    last_year_photos = (ratio_last_year / total_ratio) * total_photos
    this_year_photos = (ratio_this_year / total_ratio) * total_photos
    difference = this_year_photos - last_year_photos
    result = difference
    return result

print(solution())