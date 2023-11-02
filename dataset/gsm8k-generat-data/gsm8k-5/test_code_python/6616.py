def solution():
    total_students = 50  # Total number of students in both sections
    transferred_students = 2  # Number of students transferred from Industry to Diligence
    equal_number_of_students = total_students / 2  # Equal number of students in each section after transfers

    # Calculate the number of students in Diligence before the transfer
    diligence_students = equal_number_of_students + transferred_students
    result = diligence_students
    return result

print(solution())