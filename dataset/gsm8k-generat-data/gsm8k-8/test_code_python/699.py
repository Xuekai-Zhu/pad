def solution():
    # Calculate the number of third, fourth, and fifth grade students
    third_grade_students = 5 * 30
    fourth_grade_students = 4 * 28
    fifth_grade_students = 4 * 27

    # Calculate the total number of students
    total_students = third_grade_students + fourth_grade_students + fifth_grade_students

    # Calculate the cost of one lunch for one student
    cost_per_student = 2.10 + 0.50 + 0.20

    # Calculate the cost of one lunch for all students
    total_cost = total_students * cost_per_student
    result = total_cost
    return result

print(solution())