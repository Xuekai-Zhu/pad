def solution():
    """The number of students in Kylie's class is 50. In a particular test, ten students scored 90 marks, 15 scored ten marks fewer than the first ten students, and the rest scored 60 marks each. What are the average marks for the whole class?"""
    # Define the number of students and the number of students who scored 90 marks
    total_students = 50
    students_90 = 10

    # Calculate the number of students who scored 80 marks
    students_80 = 15

    # Calculate the total marks of the 10 students who scored 90 marks
    marks_90 = students_90 * 90

    # Calculate the total marks of the 15 students who scored 80 marks
    marks_80 = students_80 * 80

    # Calculate the total marks of the remaining students who scored 60 marks
    marks_60 = (total_students - students_90 - students_80) * 60

    # Calculate the total marks of the whole class
    total_marks = marks_90 + marks_80 + marks_60

    # Calculate the average marks for the whole class
    average_marks = total_marks / total_students

    result = average_marks
    return result

print(solution())