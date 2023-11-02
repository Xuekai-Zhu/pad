def solution():
    # Define Mandy's age when she started reading 8-page books
    age_at_8_pages = 6

    # Calculate Mandy's age when she started reading 40-page books
    age_at_40_pages = age_at_8_pages * 2

    # Calculate Mandy's age when she started reading 120-page books
    age_at_120_pages = age_at_40_pages + 8

    # Calculate Mandy's current age
    current_age = age_at_120_pages + 8

    # Calculate the length of the books Mandy currently reads
    current_book_length = 4 * (120 * 3)

    # Calculate the number of pages in the books Mandy currently reads
    current_book_pages = 8 * current_book_length

    result = current_book_pages
    return result

print(solution())