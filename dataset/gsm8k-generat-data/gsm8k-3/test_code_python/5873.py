def solution():
    """The school principal decided that she wanted every class to have an equal number of boys and girls in each first-grade classroom. There are 4 classrooms. There are 56 boys and 44 girls. How many total students are in each classroom?"""
    # Calculate the total number of students
    total_students = 56 + 44

    # Calculate the number of students per class
    students_per_class = total_students // 4

    # Display the number of students per class
    result = students_per_class
    return result

print(solution())