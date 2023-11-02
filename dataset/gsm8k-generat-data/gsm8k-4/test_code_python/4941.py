def solution():
    """Thirty students run in a charity race to raise money for the hurricane victims. Ten of the students raised $20 each. The rest of the students raised $30 each. How much did the students raise in all?"""
    # Define the number of students who raised $20
    num_students_20 = 10

    # Define the amount raised by each student who raised $20
    amount_per_student_20 = 20

    # Define the number of students who raised $30
    num_students_30 = 30 - num_students_20

    # Define the amount raised by each student who raised $30
    amount_per_student_30 = 30

    # Calculate the total amount raised
    total_amount = num_students_20 * amount_per_student_20 + num_students_30 * amount_per_student_30

    # return the result
    result = total_amount
    return result

print(solution())