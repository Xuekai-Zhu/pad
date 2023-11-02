def solution():
    """Ethan is reading a sci-fi book that has 360 pages. He read 40 pages on Saturday morning and another 10 pages at night. The next day he read twice the total pages as on Saturday. How many pages does he have left to read?"""
    # Define the total number of pages in the book
    total_pages = 360

    # Calculate the total number of pages read on Saturday
    sat_morning_pages = 40
    sat_night_pages = 10
    sat_total_pages = sat_morning_pages + sat_night_pages

    # Calculate the total number of pages read on Sunday
    sun_total_pages = sat_total_pages * 2

    # Calculate the total number of pages read
    total_read_pages = sat_total_pages + sun_total_pages

    # Calculate the number of pages left to read
    pages_left_to_read = total_pages - total_read_pages

    result = pages_left_to_read
    return result

print(solution())