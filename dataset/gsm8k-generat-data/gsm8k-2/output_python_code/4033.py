def solution():
    """Out of the 80 students who took the biology exam, only 2/5 of them managed to score 100%. If a score below 80% qualified as failing, and 50 percent of the remaining students who didn't score 100% managed to score over 80%, calculate the number of students who failed the exam."""
    total_students = 80
    perfect_scored_students = total_students * (2/5)
    remaining_students = total_students - perfect_scored_students
    failed_students = 0
    for i in range(int(remaining_students)):
        if i % 2 == 0:
            continue
        else:
            if i / remaining_students < 0.5:
                failed_students += 1
    result = failed_students
    return result

print(solution())