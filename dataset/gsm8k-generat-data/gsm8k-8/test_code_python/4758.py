def solution():
    # Determine the number of students receiving a free lunch
    free_lunch_students = 0.4 * 50

    # Determine the number of paying students
    paying_students = 50 - free_lunch_students

    # Determine the cost per paying student
    cost_per_paying_student = 210 / paying_students

    # Round the cost to the nearest cent and return the result
    result = round(cost_per_paying_student, 2)
    return result

print(solution())