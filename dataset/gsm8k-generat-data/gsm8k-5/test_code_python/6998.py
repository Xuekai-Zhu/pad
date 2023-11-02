def solution():
    total_pages = 210  # The book has 210 pages
    current_page = 90  # Jo is currently on page 90
    pages_read = current_page - 60  # Jo has read 30 pages in the last hour
    pages_remaining = total_pages - current_page  # Jo still needs to read this many pages
    pages_per_hour = 30  # Jo reads at a steady pace of 30 pages per hour

    # Calculate the total number of hours it will take Jo to finish the book
    total_hours = (pages_remaining - pages_read) / pages_per_hour

    result = total_hours
    return result

print(solution())