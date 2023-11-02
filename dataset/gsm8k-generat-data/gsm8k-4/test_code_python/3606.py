def solution():
    """In a school with 800 students, 5/8 of the students are girls. Seven-tenths of the girls and two-fifths of the boys are in the primary grades, while the rest are middle schoolers. How many middle schoolers are there?"""
    # Define the total number of students and the number of girls
    total_students = 800
    girls = total_students * 5/8

    # Calculate the number of boys
    boys = total_students - girls

    # Calculate the number of girls and boys in primary grades
    girls_primary = girls * 7/10
    boys_primary = boys * 2/5

    # Calculate the total number of students in primary grades
    total_primary = girls_primary + boys_primary

    # Calculate the number of middle schoolers
    middle_schoolers = total_students - total_primary

    # return the result
    result = middle_schoolers
    return result

print(solution())