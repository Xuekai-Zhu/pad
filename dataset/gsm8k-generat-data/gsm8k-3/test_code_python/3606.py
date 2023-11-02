def solution():
    """In a school with 800 students, 5/8 of the students are girls. Seven-tenths of the girls and two-fifths of the boys are in the primary grades, while the rest are middle schoolers. How many middle schoolers are there?"""
    # Define the total number of students and the fraction that are girls
    total_students = 800
    girls_fraction = 5/8

    # Calculate the number of girls and boys
    num_girls = girls_fraction * total_students
    num_boys = total_students - num_girls

    # Calculate the number of girls and boys in primary grades
    girls_primary = 7/10 * num_girls
    boys_primary = 2/5 * num_boys

    # Calculate the total number of students in primary grades
    total_primary = girls_primary + boys_primary

    # Calculate the number of middle schoolers
    num_middle = total_students - total_primary

    # Display the number of middle schoolers
    result = num_middle
    return result

print(solution())