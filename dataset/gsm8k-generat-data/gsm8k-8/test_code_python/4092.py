def solution():
    # Calculate the number of pages Melody will read for each class
    english_pages = 20 / 4
    science_pages = 16 / 4
    civics_pages = 8 / 4
    chinese_pages = 12 / 4

    # Calculate the total number of pages Melody will read tomorrow
    total_pages = english_pages + science_pages + civics_pages + chinese_pages
    result = total_pages
    return result

print(solution())