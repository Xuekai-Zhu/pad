def solution():
    # Calculate the total number of pages Ryan's brother read in a week
    total_brother_pages = 200 * 7  # brother got one book a day that was 200 pages each for 7 days

    # Calculate the average number of pages Ryan read per day
    ryan_pages_per_day = (2100 / 5) / 7  # Ryan got five books from the library, finished in a week

    # Calculate the average number of pages Ryan's brother read per day
    brother_pages_per_day = total_brother_pages / 7

    # Calculate the difference in pages read per day between Ryan and his brother
    difference = ryan_pages_per_day - brother_pages_per_day
    result = difference
    return result

print(solution())