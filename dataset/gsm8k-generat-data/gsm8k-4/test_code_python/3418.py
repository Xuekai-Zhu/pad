def solution():
    """Stella collects stamps. She counted 50 pages in her collector's album. There are 5 rows of 30 stamps in each of the first 10 pages of her album. The rest of the pages each have 50 stamps. How many stamps are in Stella's album?"""
    # Define the number of pages and stamps per page
    total_pages = 50
    stamps_per_page_row1_to_10 = 5 * 30
    stamps_per_page_row1_to_50_except_1_to_10 = 50

    # Calculate the total number of stamps in the first 10 pages
    stamps_in_first_10_pages = stamps_per_page_row1_to_10 * 10

    # Calculate the total number of stamps in the rest of the pages
    remaining_pages = total_pages - 10
    stamps_in_remaining_pages = stamps_per_page_row1_to_50_except_1_to_10 * remaining_pages

    # Calculate the total number of stamps in Stella's album
    total_stamps = stamps_in_first_10_pages + stamps_in_remaining_pages

    # return the result
    result = total_stamps
    return result

print(solution())