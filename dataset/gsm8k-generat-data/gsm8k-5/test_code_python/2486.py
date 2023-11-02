def solution():
    total_pages = 248  # The book has 248 pages
    pages_read_on_Monday = 16 * 3  # Joanna reads 16 pages per hour for 3 hours on Monday
    pages_read_on_Tuesday = 16 * 6.5  # Joanna reads 16 pages per hour for 6.5 hours on Tuesday
    pages_read_so_far = pages_read_on_Monday + pages_read_on_Tuesday  # Joanna has read this many pages so far

    # Calculate how many more pages Joanna needs to read to finish the book
    remaining_pages = total_pages - pages_read_so_far

    # Calculate how many more hours Joanna needs to read to finish the book, assuming she reads at the same speed of 16 pages per hour
    remaining_time = remaining_pages / 16
    result = remaining_time
    return result

print(solution())