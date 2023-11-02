def solution():
    num_students = 12
    student_cost = 1

    num_teachers = 4
    teacher_cost = 3

    # Calculate the total cost of all student tickets
    total_student_cost = num_students * student_cost

    # Calculate the total cost of all teacher tickets
    total_teacher_cost = num_teachers * teacher_cost

    # Calculate the total cost of all tickets
    total_cost = total_student_cost + total_teacher_cost
    result = total_cost
    return result

print(solution())