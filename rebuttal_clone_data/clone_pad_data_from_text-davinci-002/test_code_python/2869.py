def solution():
    total_pages = 120
    science_project = total_pages * 0.25
    math_homework = total_pages * 0.10
    remaining_pages = total_pages - (science_project + math_homework)
    result = remaining_pages
    return result

print(solution())