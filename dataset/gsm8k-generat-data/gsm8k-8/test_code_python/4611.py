def solution():
    # Calculate the number of students in the class after the new students joined
    initial_number = 160
    new_students = 20
    total_students = initial_number + new_students

    # Calculate the number of students that transferred out
    transfer_ratio = 1/3
    transferred_students = total_students * transfer_ratio

    # Calculate the final number of students in the class
    final_number = total_students - transferred_students
    result = final_number
    return result

print(solution())