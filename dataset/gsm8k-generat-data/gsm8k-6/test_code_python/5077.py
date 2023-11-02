def solution():
    # Calculate the number of pages Lance needs to read to finish the book
    remaining_pages = 100 - 35 - (35 - 5)  # Lance has read 35 pages on day 1 and (35-5) pages on day 2
    pages_per_day = remaining_pages / 1  # Lance has 1 day left to finish the book
    result = pages_per_day
    return result

print(solution())