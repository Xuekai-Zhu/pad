def solution():
    """Cyrus has been contracted to write a 500 page book.  On his first day, he writes 25 pages and twice that amount on the second day.  On the third day he is able to write twice the amount that he did on the second day.  On the fourth day, he gets writer's block and is only able to write 10 pages.  How many more pages does he need to write?"""
    # Define the number of pages written on each day
    day1 = 25
    day2 = 2 * day1
    day3 = 2 * day2
    day4 = 10

    # Calculate the total number of pages written
    total_pages = day1 + day2 + day3 + day4

    # Calculate the number of pages left to write
    pages_left = 500 - total_pages

    # Display the number of pages left to write
    result = pages_left
    return result

print(solution())