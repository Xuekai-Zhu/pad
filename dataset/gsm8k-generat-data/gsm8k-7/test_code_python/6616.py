def solution():
    total_students = 50

    # Since 2 students were transferred from Industry to Diligence, we can assume they had equal number of students before the transfer
    # So, let's represent the number of students in Diligence as x, and Industry as x+2
    x = (total_students - 2) // 2
    num_students_diligence = x
    result = num_students_diligence
    return result

print(solution())