def solution():
    num_students = 15

    # Calculate the total number of pages from the first 5 students
    total_pages_first_5 = 5 * 2

    # Calculate the total number of pages from the next 5 students
    total_pages_next_5 = 5 * 3

    # Calculate the total number of pages from the last 5 students
    total_pages_last_5 = 5 * 1

    # Calculate the total number of pages from all students
    total_pages = total_pages_first_5 + total_pages_next_5 + total_pages_last_5

    # Calculate the average page count per essay
    avg_pages_per_essay = total_pages / num_students
    result = avg_pages_per_essay
    return result

print(solution())