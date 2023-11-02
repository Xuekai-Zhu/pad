def solution():
    students = 15
    essays_2_pages = 5
    essays_3_pages = 5
    essays_1_page = 5
    total_pages = (essays_2_pages * 2) + (essays_3_pages * 3) + (essays_1_page * 1)
    average_pages = total_pages / students
    result = average_pages
    return result

print(solution())