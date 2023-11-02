def solution():
    book1_pages = 180
    book2_pages = 100
    total_weeks = 2
    total_days = total_weeks * 7

    # Calculate the total number of pages Yasna needs to read
    total_pages = book1_pages + book2_pages

    # Calculate the number of pages Yasna needs to read every day
    daily_pages = total_pages / total_days
    result = daily_pages
    return result

print(solution())