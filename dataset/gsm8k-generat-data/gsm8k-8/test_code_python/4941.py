def solution():
    # Define the number of students who raised $20
    num_students_20 = 10

    # Calculate the amount raised by those students
    amount_20 = num_students_20 * 20

    # Define the number of students who raised $30
    num_students_30 = 30 - num_students_20

    # Calculate the amount raised by those students
    amount_30 = num_students_30 * 30

    # Calculate the total amount raised
    total_amount = amount_20 + amount_30
    result = total_amount
    return result

print(solution())