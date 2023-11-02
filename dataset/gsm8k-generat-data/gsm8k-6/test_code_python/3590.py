def solution():
    # Calculate the number of pages Hallie read on each day
    pages_read_day1 = 63
    pages_read_day2 = 2 * pages_read_day1
    pages_read_day3 = pages_read_day2 + 10
    pages_read_day4 = 354 - (pages_read_day1 + pages_read_day2 + pages_read_day3)  # total pages read must equal the length of the book

    result = pages_read_day4
    return result

print(solution())