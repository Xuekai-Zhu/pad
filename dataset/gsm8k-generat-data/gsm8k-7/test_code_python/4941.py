def solution():
    num_students = 30
    num_students_raised_20 = 10
    num_students_raised_30 = num_students - num_students_raised_20
    amount_raised_20 = 20
    amount_raised_30 = 30

    # Calculate the total amount raised by students who raised $20 each
    total_raised_20 = num_students_raised_20 * amount_raised_20

    # Calculate the total amount raised by students who raised $30 each
    total_raised_30 = num_students_raised_30 * amount_raised_30

    # Calculate the total amount raised by all students
    total_raised = total_raised_20 + total_raised_30
    result = total_raised
    return result

print(solution())