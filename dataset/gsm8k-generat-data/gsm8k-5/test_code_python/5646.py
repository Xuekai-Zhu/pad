def solution():
    pages_read_per_week = 100 * 3  # Steve reads 100 pages on Monday, Wednesday, and Friday
    total_pages = 2100  # The book is 2100 pages long

    # Calculate the total number of weeks it will take to read the book
    weeks_to_read = total_pages / pages_read_per_week
    result = weeks_to_read
    return result

print(solution())