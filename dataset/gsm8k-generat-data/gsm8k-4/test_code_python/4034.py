def solution():
    """Out of the 80 students who took the biology exam, only 2/5 of them managed to score 100%. If a score below 80% qualified as failing, and 50 percent of the remaining students who didn't score 100% managed to score over 80%, calculate the number of students who failed the exam."""
    # Define the number of students who took the exam
    total_students = 80

    # Calculate the number of students who scored 100%
    perfect_score_students = total_students * (2/5)

    # Calculate the number of students who didn't score 100%
    other_students = total_students - perfect_score_students

    # Calculate the number of students who scored over 80%
    over_80_students = (other_students * 0.5) * 0.5

    # Calculate the number of students who failed
    failed_students = other_students - over_80_students

    # Return the result
    result = int(failed_students)
    return result

print(solution())