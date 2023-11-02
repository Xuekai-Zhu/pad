def solution():
    
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