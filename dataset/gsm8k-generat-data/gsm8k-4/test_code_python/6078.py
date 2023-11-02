def solution():
    """Cyrus has been contracted to write a 500 page book.  On his first day, he writes 25 pages and twice that amount on the second day.  On the third day he is able to write twice the amount that he did on the second day.  On the fourth day, he gets writer's block and is only able to write 10 pages.  How many more pages does he need to write?"""
    # Define the total number of pages in the book and initialize the total number of pages written
    total_pages = 500
    pages_written = 0

    # Write on the first day
    pages_written += 25

    # Write on the second day
    pages_written += 2 * 25

    # Write on the third day
    pages_written += 2 * 2 * 25

    # Write on the fourth day
    pages_written += 10

    # Calculate the remaining number of pages to write
    remaining_pages = total_pages - pages_written

    # Display the result
    result = remaining_pages
    return result

print(solution())