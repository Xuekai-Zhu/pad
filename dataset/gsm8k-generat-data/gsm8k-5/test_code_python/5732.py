def solution():
    total_students = 50  # The number of students in Kylie's class
    top_scorers = 10  # Ten students scored 90 marks
    mid_scorers = 15  # 15 students scored ten marks fewer than the top scorers
    low_scorers = total_students - top_scorers - mid_scorers  # The rest scored 60 marks each

    # Calculate the total marks obtained by the class
    total_marks = (top_scorers * 90) + (mid_scorers * 80) + (low_scorers * 60)

    # Calculate the average marks obtained by the whole class
    average_marks = total_marks / total_students
    result = average_marks
    return result

print(solution())