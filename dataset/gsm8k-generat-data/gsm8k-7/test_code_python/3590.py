def solution():
    book_length = 354
    day1_reading = 63
    day2_reading = 2 * day1_reading
    day3_reading = day2_reading + 10

    # Calculate the total pages read in the first three days
    total_reading = day1_reading + day2_reading + day3_reading

    # Calculate the number of pages left to read
    pages_left = book_length - total_reading

    # Calculate the number of pages Hallie read on the fourth day
    day4_reading = pages_left / (4 - 3)

    result = day4_reading
    return result

print(solution())