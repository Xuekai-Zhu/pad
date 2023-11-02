def solution():
    """A classroom of 15 students turned in essays on Friday morning. The first 5 students each turned in essays with 2 pages. The next 5 students each turned in essays with 3 pages. The last 5 students each turned in essays with 1 page. What is the average page count per essay for the 15 students?"""
    # Define the number of students and pages per essay for each group
    num_students = 15
    group1_pages = 2
    group2_pages = 3
    group3_pages = 1

    # Calculate the total number of pages
    total_pages = (5 * group1_pages) + (5 * group2_pages) + (5 * group3_pages)

    # Calculate the average number of pages per essay
    avg_pages = total_pages / num_students
    
    # Display the average number of pages per essay
    result = avg_pages
    return result

print(solution())