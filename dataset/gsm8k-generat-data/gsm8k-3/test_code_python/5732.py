def solution():
    """The number of students in Kylie's class is 50. In a particular test, ten students scored 90 marks, 15 scored ten marks fewer than the first ten students, and the rest scored 60 marks each. What are the average marks for the whole class?"""
    # Define the number of students in the class
    total_students = 50

    # Define the number of students who scored 90 marks
    high_scorers = 10

    # Define the number of students who scored 10 marks less than the high scorers
    medium_scorers = 15

    # Define the number of students who scored 60 marks
    low_scorers = total_students - high_scorers - medium_scorers

    # Calculate the total marks for the high scorers
    high_marks = high_scorers * 90

    # Calculate the total marks for the medium scorers
    medium_marks = medium_scorers * 80

    # Calculate the total marks for the low scorers
    low_marks = low_scorers * 60

    # Calculate the total marks for the whole class
    total_marks = high_marks + medium_marks + low_marks

    # Calculate the average marks for the whole class
    average_marks = total_marks / total_students

    # Display the average marks for the whole class
    result = average_marks
    return result

print(solution())