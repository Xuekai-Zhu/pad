def solution():
    """John writes 20 pages a day. How long will it take him to write 3 books that are 400 pages each?"""
    # Define the number of pages John can write per day
    pages_per_day = 20

    # Define the number of pages in each book
    pages_per_book = 400

    # Define the number of books John needs to write
    num_books = 3

    # Calculate the total number of pages John needs to write
    total_pages = pages_per_book * num_books

    # Calculate the number of days it will take John to write all the pages
    num_days = total_pages / pages_per_day

    # Return the result
    result = num_days
    return result

print(solution())