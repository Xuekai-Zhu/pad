def solution():
    third_graders = 20  # Ms. Hatcher teaches 20 third-graders
    fourth_graders = 2 * third_graders  # The number of fourth-graders is twice the number of third-graders
    fifth_graders = third_graders / 2  # The fifth-grade class has half as many students as the number of third-graders

    # Calculate the total number of students Ms. Hatcher taught for the day
    total_students = third_graders + fourth_graders + fifth_graders
    result = total_students
    return result

print(solution())