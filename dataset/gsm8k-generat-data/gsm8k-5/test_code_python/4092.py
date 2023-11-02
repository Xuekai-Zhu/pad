def solution():
    english_pages = 20
    science_pages = 16
    civics_pages = 8
    chinese_pages = 12

    # Calculate the number of pages Melody will read for each class tomorrow
    english_pages_tomorrow = english_pages / 4
    science_pages_tomorrow = science_pages / 4
    civics_pages_tomorrow = civics_pages / 4
    chinese_pages_tomorrow = chinese_pages / 4

    # Calculate the total number of pages Melody will read tomorrow
    total_pages_tomorrow = english_pages_tomorrow + science_pages_tomorrow + civics_pages_tomorrow + chinese_pages_tomorrow

    result = total_pages_tomorrow
    return result

print(solution())