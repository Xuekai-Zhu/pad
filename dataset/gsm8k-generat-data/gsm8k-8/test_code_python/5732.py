def solution():
    # Define the number of students in the class and the scores for each group
    total_students = 50
    group1_score = 90
    group2_score = group1_score - 10
    group2_size = 15

    # Calculate the total score for all students
    total_score = group1_score * 10 + group2_score * group2_size + 60 * (total_students - 10 - group2_size)

    # Calculate the average score for the whole class
    average_score = total_score / total_students
    result = average_score
    return result

print(solution())