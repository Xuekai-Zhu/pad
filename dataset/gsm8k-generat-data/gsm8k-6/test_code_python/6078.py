def solution():
    # Calculate the total number of pages written by Cyrus in four days
    pages_day1 = 25
    pages_day2 = 2 * pages_day1
    pages_day3 = 2 * pages_day2
    pages_day4 = 10
    total_pages_written = pages_day1 + pages_day2 + pages_day3 + pages_day4

    # Calculate the number of pages Cyrus still needs to write
    pages_left = 500 - total_pages_written
    result = pages_left
    return result

print(solution())