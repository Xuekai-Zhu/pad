def solution():
    # Calculate the average number of pages Ryan read per day
    ryan_total_pages = 2100
    ryan_days = 5
    ryan_avg_pages = ryan_total_pages / ryan_days

    # Calculate the total number of pages Ryan's brother read
    brother_total_pages = 200 * 7

    # Calculate the difference in average pages per day
    difference = ryan_avg_pages - (brother_total_pages / 7)

    result = difference
    return result

print(solution())