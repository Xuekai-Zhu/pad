def solution():
    """Jane had a 500 page book to read. The first half of the book Jane read with a speed of 10 pages per day, and the second half with a speed of 5 pages a day. How many days did Jane spend reading this book?"""
    total_pages = 500
    first_half_pages = total_pages / 2
    second_half_pages = total_pages / 2
    first_half_days = first_half_pages / 10
    second_half_days = second_half_pages / 5
    total_days = first_half_days + second_half_days
    result = total_days
    return result

print(solution())