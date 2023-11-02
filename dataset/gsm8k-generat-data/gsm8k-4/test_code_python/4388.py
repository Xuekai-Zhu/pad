def solution():
    """A classroom of 15 students turned in essays on Friday morning. The first 5 students each turned in essays with 2 pages. The next 5 students each turned in essays with 3 pages. The last 5 students each turned in essays with 1 page. What is the average page count per essay for the 15 students?"""
    # Define the number of students in each group
    group_size = 5

    # Define the number of pages per essay in each group
    group1_pages = 2
    group2_pages = 3
    group3_pages = 1

    # Calculate the total number of pages for each group
    group1_total_pages = group1_pages * group_size
    group2_total_pages = group2_pages * group_size
    group3_total_pages = group3_pages * group_size

    # Calculate the total number of pages for all essays
    total_pages = group1_total_pages + group2_total_pages + group3_total_pages

    # Calculate the average page count per essay
    average_pages = total_pages / 15

    # return the result
    result = average_pages
    return result

print(solution())