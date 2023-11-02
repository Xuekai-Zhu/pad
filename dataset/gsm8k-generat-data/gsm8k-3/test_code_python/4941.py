def solution():
    """Thirty students run in a charity race to raise money for the hurricane victims. Ten of the students raised $20 each. The rest of the students raised $30 each. How much did the students raise in all?"""
    # Define the number of students who raised $20 and the amount they raised
    num_students_20 = 10
    amt_per_student_20 = 20

    # Define the number of students who raised $30
    num_students_30 = 30 - num_students_20

    # Calculate the total amount raised by the students
    total_raised = num_students_20 * amt_per_student_20 + num_students_30 * 30

    # Display the total amount raised
    result = total_raised
    return result

print(solution())