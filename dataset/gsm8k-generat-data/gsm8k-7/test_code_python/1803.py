def solution():
    total_students = 90
    cafeteria_percent = 2/3
    outside_percent = 1/3

    # Calculate the number of students in the cafeteria and outside initially
    cafeteria_students = total_students * cafeteria_percent
    outside_students = total_students * outside_percent

    # Calculate the number of students who went inside the cafeteria and outside
    students_inside = outside_students * 1/3
    students_outside = cafeteria_students * 3/90

    # Calculate the final number of students in the cafeteria
    final_cafeteria_students = cafeteria_students + students_inside - students_outside
    result = final_cafeteria_students
    return result

print(solution())