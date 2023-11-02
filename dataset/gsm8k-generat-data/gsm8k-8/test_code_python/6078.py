def solution():
    # Define the number of pages written on each day
    day1 = 25
    day2 = 2 * day1
    day3 = 2 * day2
    day4 = 10

    # Calculate the total number of pages written
    total_pages = day1 + day2 + day3 + day4

    # Calculate the number of pages remaining to be written
    remaining_pages = 500 - total_pages
    result = remaining_pages
    return result

print(solution())