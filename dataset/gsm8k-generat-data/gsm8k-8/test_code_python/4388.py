def solution():
    # Define the number of students in each group and the number of pages per essay
    group1_students = 5
    group1_pages = 2
    group2_students = 5
    group2_pages = 3
    group3_students = 5
    group3_pages = 1

    # Calculate the total number of pages and essays
    total_pages = (group1_students * group1_pages) + (group2_students * group2_pages) + (group3_students * group3_pages)
    total_essays = group1_students + group2_students + group3_students

    # Calculate the average page count per essay
    average_page_count = total_pages / total_essays
    result = average_page_count
    return result

print(solution())