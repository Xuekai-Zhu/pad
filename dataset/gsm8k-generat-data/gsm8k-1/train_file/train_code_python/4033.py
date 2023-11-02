def solution():
    """Out of the 80 students who took the biology exam, only 2/5 of them managed to score 100%. If a score below 80% qualified as failing, and 50 percent of the remaining students who didn't score 100% managed to score over 80%, calculate the number of students who failed the exam."""
    total_students = 80
    perfect_scored = total_students * (2/5)
    remaining_students = total_students - perfect_scored
    over_80_scored = remaining_students * 0.5
    failed_students = total_students - (perfect_scored + over_80_scored)
    result = failed_students
    return result

print(solution())