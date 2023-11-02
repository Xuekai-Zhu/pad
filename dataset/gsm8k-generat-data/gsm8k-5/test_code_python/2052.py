def solution():
    total_pages = 500  # Jane had a 500 page book to read
    half_pages = int(total_pages / 2)  # We need to know how many pages are in half the book

    # Calculate the number of days it took Jane to read the first half of the book
    days_first_half = int(half_pages / 10)

    # Calculate the number of days it took Jane to read the second half of the book
    days_second_half = int(half_pages / 5)

    # Calculate the total number of days Jane spent reading the book
    total_days = days_first_half + days_second_half
    result = total_days
    return result

print(solution())