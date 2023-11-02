def solution():
    num_hands = 20
    hands_per_student = 2

    # Calculate the total number of students in the class
    total_students = num_hands / hands_per_student

    # Add Peter to the total number of students
    total_students += 1

    result = total_students
    return result

print(solution())