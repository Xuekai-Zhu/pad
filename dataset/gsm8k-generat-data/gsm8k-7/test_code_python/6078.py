def solution():
    total_pages = 500
    day_one = 25
    day_two = day_one * 2
    day_three = day_two * 2
    day_four = 10

    # Calculate the total number of pages written so far
    total_written = day_one + day_two + day_three + day_four

    # Calculate the number of pages left to write
    pages_left = total_pages - total_written
    result = pages_left
    return result

print(solution())