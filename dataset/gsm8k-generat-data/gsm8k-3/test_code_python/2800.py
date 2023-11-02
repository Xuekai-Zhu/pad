def solution():
    """There are 20 boys and 11 girls in the second grade and twice that number in the third grade. How many students are in grades 2 and 3?"""
    # Define the number of boys and girls in second grade
    boys_2 = 20
    girls_2 = 11

    # Calculate the total number of students in second grade
    students_2 = boys_2 + girls_2

    # Calculate the number of students in third grade
    students_3 = 2 * students_2

    # Calculate the total number of students in grades 2 and 3
    total_students = students_2 + students_3

    # Display the total number of students
    result = total_students
    return result

print(solution())