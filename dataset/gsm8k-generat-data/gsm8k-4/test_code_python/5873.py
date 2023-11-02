def solution():
    """The school principal decided that she wanted every class to have an equal number of boys and girls in each first-grade classroom. There are 4 classrooms. There are 56 boys and 44 girls. How many total students are in each classroom?"""
    # Define the number of boys and girls
    num_boys = 56
    num_girls = 44

    # Calculate the total number of students
    total_students = num_boys + num_girls

    # Calculate the number of students per classroom
    students_per_classroom = total_students / 4

    # return the result
    result = students_per_classroom
    return result

print(solution())