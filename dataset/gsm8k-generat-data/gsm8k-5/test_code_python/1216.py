def solution():
    total_deserts = 14 + 12  # There are 14 mini-cupcakes and 12 donut holes
    num_students = 13  # There are 13 students in the class

    # Calculate how many deserts each student gets
    deserts_per_student = total_deserts // num_students
    result = deserts_per_student
    return result

print(solution())