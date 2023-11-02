def solution():
    # Calculate total amount raised by the 10 students who raised $20 each
    ten_student_amount = 10 * 20

    # Calculate total amount raised by the remaining students who raised $30 each
    remaining_students = 30 - 10  # 10 students already accounted for 
    remaining_amount = remaining_students * 30

    # Calculate total amount raised by all students
    total_amount = ten_student_amount + remaining_amount
    result = total_amount
    return result

print(solution())