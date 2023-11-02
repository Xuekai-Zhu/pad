def solution():
    age_to_begin_breast_exam = 20
    age_of_middle_school_students = [11, 12, 13, 14, 15, 16]
    if age_to_begin_breast_exam not in age_of_middle_school_students:
        result = "no"
    else:
        result = "not applicable"
    return result

(Note: The answer is "no" because middle school students are not typically of the age to begin breast exams.)

print(solution())