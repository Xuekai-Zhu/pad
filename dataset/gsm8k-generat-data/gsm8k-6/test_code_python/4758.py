def solution():
    # Find the number of students receiving free lunch and the number of paying students
    total_students = 50
    free_lunch_students = 0.4 * total_students
    paying_students = total_students - free_lunch_students

    # Find the cost per paying student
    cost_per_paying_student = 210 / paying_students
    result = cost_per_paying_student
    return result

print(solution())