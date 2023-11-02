def solution():
    total_pages = 354  # The book is 354 pages long
    day1 = 63  # Hallie read 63 pages on the first day
    day2 = 2 * day1  # Hallie read twice the number of pages on the second day as she did on the first
    day3 = day2 + 10  # Hallie read 10 more pages on the third day than she did on the second
    pages_read_so_far = day1 + day2 + day3  # Hallie has read this many pages so far
    pages_left = total_pages - pages_read_so_far  # Hallie has this many pages left to read
    pages_day4 = pages_left / 1  # Hallie reads the remaining pages on the fourth day
    result = pages_day4
    return result

print(solution())