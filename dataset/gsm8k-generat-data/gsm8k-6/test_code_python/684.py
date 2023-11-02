def solution():
    # Calculate the time it would take Grace to read a 250-page book
    # using the ratio of pages to time for the 200-page book
    time_200_pages = 20  # hours to read a 200-page book
    pages_per_hour = 200/20  # pages read per hour
    time_250_pages = 250/pages_per_hour
    result = time_250_pages
    return result

print(solution())