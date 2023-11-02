def solution():
    """Stella collects stamps. She counted 50 pages in her collector's album. There are 5 rows of 30 stamps in each of the first 10 pages of her album. The rest of the pages each have 50 stamps. How many stamps are in Stella's album?"""
    stamps_per_first_10_pages = 5 * 30 * 10
    stamps_per_remaining_pages = 50 * (50 - 10)
    total_stamps = stamps_per_first_10_pages + stamps_per_remaining_pages
    result = total_stamps
    return result

print(solution())