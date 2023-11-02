def solution():
    """Melody needs to read 20 pages for her English class, 16 pages for her Science class, 8 pages for her Civics, and 12 pages for Chinese class. She decided to read one-fourth of the number of pages for each class tomorrow. How many pages will she read tomorrow?"""
    english_pages = 20
    science_pages = 16
    civics_pages = 8
    chinese_pages = 12
    total_pages = english_pages + science_pages + civics_pages + chinese_pages
    tomorrow_pages = total_pages / 4
    result = tomorrow_pages
    return result

print(solution())