def solution():
    """Miss Grayson's class raised $50 for their field trip. Aside from that, each of her students contributed $5 each. There are 20 students in her class, and the cost of the trip is $7 for each student. After all the field trip costs were paid, how much is left in Miss Grayson's class fund?"""
    # Define the initial fund and the number of students
    initial_fund = 50
    num_students = 20

    # Calculate the total amount contributed by the students
    total_student_contrib = num_students * 5

    # Calculate the total cost of the field trip
    total_cost = num_students * 7

    # Calculate the remaining fund after paying for the field trip
    remaining_fund = initial_fund + total_student_contrib - total_cost

    result = remaining_fund
    return result

print(solution())