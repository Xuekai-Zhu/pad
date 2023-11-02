def solution():
    """Melody needs to read 20 pages for her English class, 16 pages for her Science class, 8 pages for her Civics, and 12 pages for Chinese class. She decided to read one-fourth of the number of pages for each class tomorrow. How many pages will she read tomorrow?"""
    # Define the number of pages for each class
    english_pages = 20
    science_pages = 16
    civics_pages = 8
    chinese_pages = 12

    # Calculate the number of pages to read for each class tomorrow
    english_pages_tomorrow = english_pages * 0.25
    science_pages_tomorrow = science_pages * 0.25
    civics_pages_tomorrow = civics_pages * 0.25
    chinese_pages_tomorrow = chinese_pages * 0.25

    # Calculate the total number of pages to read tomorrow
    total_pages_tomorrow = english_pages_tomorrow + science_pages_tomorrow + civics_pages_tomorrow + chinese_pages_tomorrow

    # Return the result
    result = total_pages_tomorrow
    return result

print(solution())