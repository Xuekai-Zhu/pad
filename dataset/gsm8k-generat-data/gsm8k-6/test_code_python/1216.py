def solution():
    # Calculate the total number of desserts
    total_desserts = 14 + 12  # the teacher brings in 14 mini-cupcakes and 12 donut holes

    # Calculate the number of desserts each student gets
    desserts_per_student = total_desserts // 13  # the desserts are distributed equally among the 13 students
    result = desserts_per_student
    return result

print(solution())