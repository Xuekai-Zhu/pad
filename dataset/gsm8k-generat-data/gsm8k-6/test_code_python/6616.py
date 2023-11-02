def solution():
    # Calculate the number of students in each section after the transfer
    total_students = 50
    equal_students = total_students / 2
    diligence_students = equal_students + 1  # 2 students were transferred from Industry to Diligence
    industry_students = equal_students - 2

    # Calculate the number of students in Diligence before the transfer
    students_before_transfer = diligence_students - 1

    result = students_before_transfer
    return result

print(solution())