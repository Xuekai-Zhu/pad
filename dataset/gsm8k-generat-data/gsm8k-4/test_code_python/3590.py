def solution():
    """Hallie borrows a book from the library. She reads the entire book in four days. She read 63 pages the first day. On the second day, she read twice the number of pages that she'd read on day one. On the third day, she read 10 mores pages than she read on day two. If the book is 354 pages long, how many pages did she read on the fourth day?"""
    # Define the length of the book and the pages read on the first day
    book_length = 354
    day_one_pages = 63

    # Calculate the pages read on the second and third day
    day_two_pages = day_one_pages * 2
    day_three_pages = day_two_pages + 10

    # Calculate the pages read on the first three days
    first_three_days = day_one_pages + day_two_pages + day_three_pages

    # Calculate the pages read on the fourth day by subtracting the pages read on the first three days from the total length of the book
    day_four_pages = book_length - first_three_days

    # Return the pages read on the fourth day
    result = day_four_pages
    return result

print(solution())