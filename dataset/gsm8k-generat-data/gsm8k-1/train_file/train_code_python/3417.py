def solution():
    """Stella collects stamps. She counted 50 pages in her collector's album. There are 5 rows of 30 stamps in each of the first 10 pages of her album. The rest of the pages each have 50 stamps. How many stamps are in Stella's album?"""
    first_10_pages = 10 * 5 * 30
    remaining_pages = (50 - 10) * 50
    total_stamps = first_10_pages + remaining_pages
    result = total_stamps
    return result

print(solution())