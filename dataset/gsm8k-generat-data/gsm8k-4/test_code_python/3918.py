def solution():
    """Jesse is desperately trying to finish a book for a school book report due on Monday so he can play this weekend. Friday afternoon, he read the first 5 chapters, which were 10, 15, 27, 12, and 19 pages, respectively, before taking a break. To his dismay, he found that he was only 1/3 of the way through the book. How many pages does he still have to read?"""
    # Define the total number of pages Jesse needs to read
    total_pages = None

    # Define the number of pages Jesse read on Friday
    friday_pages = sum([10, 15, 27, 12, 19])

    # Calculate the fraction of the book that Jesse has to read
    fraction_remaining = 2/3

    # Calculate the total number of pages in the book
    total_pages = friday_pages / (1/3)

    # Subtract the pages Jesse has already read from the total
    pages_remaining = total_pages - friday_pages

    result = pages_remaining
    return result

print(solution())