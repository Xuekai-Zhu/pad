def solution():
    # Calculate the total number of pages turned in by the first 5 students
    pages_first_five = 5 * 2

    # Calculate the total number of pages turned in by the next 5 students
    pages_next_five = 5 * 3

    # Calculate the total number of pages turned in by the last 5 students
    pages_last_five = 5 * 1

    # Calculate the total number of pages turned in by all 15 students
    total_pages = pages_first_five + pages_next_five + pages_last_five

    # Calculate the average page count per essay
    average_page_count = total_pages / 15
    result = average_page_count
    return result

print(solution())