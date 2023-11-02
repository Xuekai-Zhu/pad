def solution():
    
    english_pages = 20
    science_pages = 16
    civics_pages = 8
    chinese_pages = 12
    total_pages = english_pages + science_pages + civics_pages + chinese_pages
    pages_to_read_tomorrow = total_pages / 4
    result = pages_to_read_tomorrow
    return result

print(solution())