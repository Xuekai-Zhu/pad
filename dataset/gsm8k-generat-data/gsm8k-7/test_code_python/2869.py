def solution():
    total_pages = 120
    science_project_pages = total_pages * 0.25
    math_homework_pages = 10

    # Calculate the total number of pages used for science project and math homework
    total_used_pages = science_project_pages + math_homework_pages

    # Calculate the total number of pages remaining
    remaining_pages = total_pages - total_used_pages
    result = remaining_pages
    return result

print(solution())