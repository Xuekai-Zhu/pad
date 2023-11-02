def solution():
    """Hallie borrows a book from the library. She reads the entire book in four days.
    She read 63 pages the first day. On the second day, she read twice the number of pages that she'd read on day one.
    On the third day, she read 10 mores pages than she read on day two. If the book is 354 pages long,
    how many pages did she read on the fourth day?"""
    book_length = 354
    day_1 = 63
    day_2 = day_1 * 2
    day_3 = day_2 + 10
    total_first_three_days = day_1 + day_2 + day_3
    day_4 = book_length - total_first_three_days
    result = day_4
    return result

print(solution())