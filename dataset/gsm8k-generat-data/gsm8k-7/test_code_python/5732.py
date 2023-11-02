def solution():
    num_students = 50
    num_top_scorers = 10
    top_scorer_marks = 90
    lower_scorer_marks = top_scorer_marks - 10
    remaining_students_marks = 60

    # Calculate the total marks of the top 10 scorers
    top_scorers_total = num_top_scorers * top_scorer_marks

    # Calculate the total marks of the next 15 students
    lower_scorers_total = (num_students - num_top_scorers - (num_students - num_top_scorers - 15)) * lower_scorer_marks

    # Calculate the total marks of the remaining students
    remaining_students_total = (num_students - num_top_scorers - 15) * remaining_students_marks

    # Calculate the total marks of the entire class
    total_marks = top_scorers_total + lower_scorers_total + remaining_students_total

    # Calculate the average marks for the whole class
    avg_marks = total_marks / num_students
    result = avg_marks
    return result

print(solution())