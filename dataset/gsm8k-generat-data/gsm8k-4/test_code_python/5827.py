def solution():
    """Yesterday Ryan got five books from the library. They were a total of 2100 pages. His brother got one book a day that was 200 pages each. They both finished them in a week. On average, how many more pages per day did Ryan read compared to his brother?"""
    # Calculate the average number of pages Ryan read per day
    ryan_pages_per_day = 2100 / 5

    # Calculate the total number of pages Ryan's brother read in a week
    brother_total_pages = 200 * 7

    # Calculate the average number of pages Ryan's brother read per day
    brother_pages_per_day = brother_total_pages / 7

    # Calculate the difference in the average number of pages read per day by Ryan and his brother
    difference = ryan_pages_per_day - brother_pages_per_day

    # Return the result
    result = difference
    return result

print(solution())