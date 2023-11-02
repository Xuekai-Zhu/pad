def solution():
    liza_pages_per_hour = 20
    suzie_pages_per_hour = 15
    num_hours = 3

    # Calculate the total number of pages read by Liza in 3 hours
    liza_total_pages = liza_pages_per_hour * num_hours

    # Calculate the total number of pages read by Suzie in 3 hours
    suzie_total_pages = suzie_pages_per_hour * num_hours

    # Calculate the difference in pages read between Liza and Suzie
    pages_difference = liza_total_pages - suzie_total_pages
    result = pages_difference
    return result

print(solution())