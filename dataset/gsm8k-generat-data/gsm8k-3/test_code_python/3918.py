def solution():
    """Jesse is desperately trying to finish a book for a school book report due on Monday so he can play this weekend. Friday afternoon, he read the first 5 chapters, which were 10, 15, 27, 12, and 19 pages, respectively, before taking a break. To his dismay, he found that he was only 1/3 of the way through the book. How many pages does he still have to read?"""
    # Define the number of pages Jesse read on Friday afternoon
    pages_read = 10 + 15 + 27 + 12 + 19

    # Calculate the total number of pages in the book
    total_pages = pages_read * 3

    # Calculate the number of pages Jesse still needs to read
    pages_left = total_pages - pages_read

    # Display the number of pages Jesse still needs to read
    result = pages_left
    return result

print(solution())