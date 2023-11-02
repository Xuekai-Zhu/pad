def solution():
    # Calculate the number of students currently in the class
    current_students = 6 * 3

    # Calculate the number of students who went to the bathroom
    bathroom_students = 3

    # Calculate the number of students who went to the canteen
    canteen_students = 3 * 3

    # Calculate the number of students added to the class
    added_students = 2 * 4

    # Calculate the number of foreign exchange students added to the class
    exchange_students = 3 + 3 + 3

    # Calculate the total number of students in the class
    total_students = current_students + canteen_students + added_students + exchange_students - bathroom_students

    result = total_students
    return result

print(solution())