def solution():
    """Miss Grayson's class raised $50 for their field trip. Aside from that, each of her students contributed $5 each. There are 20 students in her class, and the cost of the trip is $7 for each student. After all the field trip costs were paid, how much is left in Miss Grayson's class fund?"""
    # Define the initial amount raised and the amount contributed by each student
    INITIAL_AMOUNT = 50
    STUDENT_CONTRIBUTION = 5

    # Define the number of students and the cost of the trip per student
    num_students = 20
    cost_per_student = 7

    # Calculate the total amount raised
    total_raised = INITIAL_AMOUNT + (num_students * STUDENT_CONTRIBUTION)

    # Calculate the total cost of the field trip
    total_cost = num_students * cost_per_student

    # Calculate the amount left in the class fund after the field trip
    leftover_fund = total_raised - total_cost

    # Display the amount left in the class fund
    result = Display
    return result

print(solution())