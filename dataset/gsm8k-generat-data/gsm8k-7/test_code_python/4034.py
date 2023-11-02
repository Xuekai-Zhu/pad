def solution():
    total_students = 80
    perfect_score_students = (2/5) * total_students
    remaining_students = total_students - perfect_score_students

    # Calculate the number of students who scored over 80%
    over_80_percent = 0.5 * remaining_students

    # Calculate the number of students who failed
    num_failed = remaining_students - over_80_percent

    result = num_failed
    return result

print(solution())