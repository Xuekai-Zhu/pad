def solution():
    biology_students = 80  # Total number of students who took the biology exam
    perfect_score = biology_students * (2/5)  # Number of students who scored 100%
    remaining_students = biology_students - perfect_score  # Number of students who didn't score 100%
    passing_score = 0.8  # Passing score is 80%

    # Number of students who scored over 80%
    over_80_percent = (remaining_students * 0.5) * (1 - perfect_score/biology_students)

    # Number of students who failed the exam
    failed_students = biology_students - perfect_score - over_80_percent

    result = failed_students
    return result

print(solution())