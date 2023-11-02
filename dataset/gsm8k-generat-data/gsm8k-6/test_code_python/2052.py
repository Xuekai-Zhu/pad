def solution():
    total_pages = 500  # total number of pages in the book
    first_half_pages = total_pages/2  # number of pages in the first half of the book
    second_half_pages = total_pages/2  # number of pages in the second half of the book

    # Calculate the number of days Jane spent reading the book
    days_spent = (first_half_pages/10) + (second_half_pages/5)  # Jane reads first half at 10 pages per day, second half at 5 pages per day
    result = days_spent
    return result

print(solution())