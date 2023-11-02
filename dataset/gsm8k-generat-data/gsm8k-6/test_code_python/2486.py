def solution():
    # Calculate the total number of pages read by Joanna
    pages_read = 16 * (3 + 6.5)  # Joanna reads 16 pages per hour on both days
    remaining_pages = 248 - pages_read  # Calculate the remaining number of pages
    hours_needed = remaining_pages/16  # Calculate the number of hours needed to read the remaining pages
    result = hours_needed
    return result

print(solution())