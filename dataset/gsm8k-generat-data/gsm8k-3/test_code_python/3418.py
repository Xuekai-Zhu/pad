def solution():
    """Stella collects stamps. She counted 50 pages in her collector's album. There are 5 rows of 30 stamps in each of the first 10 pages of her album. The rest of the pages each have 50 stamps. How many stamps are in Stella's album?"""
    # Calculate the number of stamps on the first 10 pages
    stamps_first_10 = 5 * 30 * 10

    # Calculate the number of stamps on the remaining pages
    stamps_remaining = 50 * (50 - 10)

    # Calculate the total number of stamps in Stella's album
    total_stamps = stamps_first_10 + stamps_remaining

    # Display the total number of stamps
    result = total_stamps
    return result

print(solution())