def solution():
    """Yesterday Ryan got five books from the library. They were a total of 2100 pages. His brother got one book a day that was 200 pages each. They both finished them in a week. On average, how many more pages per day did Ryan read compared to his brother?"""
    # Calculate the average number of pages Ryan read per day
    ryan_pages_per_day = 2100/5

    # Calculate the total number of pages Ryan's brother read in a week
    brother_pages_in_week = 200*7

    # Calculate the average number of pages Ryan's brother read per day
    brother_pages_per_day = brother_pages_in_week/7

    # Calculate the difference in pages read per day
    diff_pages_per_day = ryan_pages_per_day - brother_pages_per_day

    # Display the result
    result = diff_pages_per_day
    return result

print(solution())