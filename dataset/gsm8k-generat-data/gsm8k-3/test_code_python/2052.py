def solution():
    """Jane had a 500 page book to read. The first half of the book Jane read with a speed of 10 pages per day, and the second half with a speed of 5 pages a day. How many days did Jane spend reading this book?"""
    # Define the number of pages in the book, and the reading speeds
    total_pages = 500
    speed1 = 10
    speed2 = 5

    # Calculate the number of days it takes to read the first half of the book
    half1_pages = total_pages / 2
    half1_days = half1_pages / speed1

    # Calculate the number of days it takes to read the second half of the book
    half2_pages = total_pages / 2
    half2_days = half2_pages / speed2

    # Calculate the total number of days to read the entire book
    total_days = half1_days + half2_days

    # Display the total number of days
    result = total_days
    return result

print(solution())