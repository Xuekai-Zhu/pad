def solution():
    num_cupcakes = 14
    num_donut_holes = 12
    num_students = 13
    
    # Calculate the total number of desserts
    total_desserts = num_cupcakes + num_donut_holes

    # Calculate the number of desserts each student gets
    desserts_per_student = total_desserts // num_students
    result = desserts_per_student
    return result

print(solution())