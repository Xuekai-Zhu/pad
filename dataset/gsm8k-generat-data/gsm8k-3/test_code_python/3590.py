def solution():
    """Hallie borrows a book from the library. She reads the entire book in four days. She read 63 pages the first day. On the second day, she read twice the number of pages that she'd read on day one. On the third day, she read 10 mores pages than she read on day two. If the book is 354 pages long, how many pages did she read on the fourth day?"""
    # Define the number of pages Hallie read on each day
    day1 = 63
    day2 = day1 * 2
    day3 = day2 + 10
    total_read = day1 + day2 + day3

    # Calculate the number of pages Hallie read on the fourth day
    day4 = 354 - total_read

    # Display the number of pages Hallie read on the fourth day
    result = day4
    return result

print(solution())