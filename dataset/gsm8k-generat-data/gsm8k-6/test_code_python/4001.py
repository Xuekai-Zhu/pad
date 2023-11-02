def solution():
    # Calculate the number of pages read by Liza and Suzie in 3 hours
    liza_pages = 20 * 3  # Liza reads 20 pages in an hour, so she reads 20*3 pages in 3 hours
    suzie_pages = 15 * 3  # Suzie reads 15 pages in an hour, so she reads 15*3 pages in 3 hours
    difference = liza_pages - suzie_pages  # calculate the difference in the number of pages read
    result = difference
    return result

print(solution())