def solution():
    total_students = 80
    classA_students = total_students * 0.4
    classB_students = classA_students - 21
    classC_students = total_students - classA_students - classB_students
    result = classC_students
    return result

print(solution())