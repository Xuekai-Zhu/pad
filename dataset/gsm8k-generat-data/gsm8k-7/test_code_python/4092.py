def solution():
    english_pages = 20
    science_pages = 16
    civics_pages = 8
    chinese_pages = 12

    # Calculate the number of pages Melody will read tomorrow for each class
    english_to_read = english_pages / 4
    science_to_read = science_pages / 4
    civics_to_read = civics_pages / 4
    chinese_to_read = chinese_pages / 4

    # Calculate the total number of pages Melody will read tomorrow
    total_to_read = english_to_read + science_to_read + civics_to_read + chinese_to_read
    result = total_to_read
    return result

print(solution())