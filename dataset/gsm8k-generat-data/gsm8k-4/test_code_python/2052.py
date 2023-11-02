def solution():
    """Jane had a 500 page book to read. The first half of the book Jane read with a speed of 10 pages per day, and the second half with a speed of 5 pages a day. How many days did Jane spend reading this book?"""
    # Define the total number of pages in the book
    total_pages = 500

    # Calculate the number of days taken to read the first half of the book
    first_half_days = total_pages/2 / 10

    # Calculate the number of days taken to read the second half of the book
    second_half_days = total_pages/2 / 5

    # Calculate the total number of days taken to read the book
    total_days = first_half_days + second_half_days

    # Return the result
    result = total_days
    return result

print(solution())