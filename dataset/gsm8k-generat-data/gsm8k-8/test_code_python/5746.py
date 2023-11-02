def solution():
    # Define the number of students and teachers
    num_students = 12
    num_teachers = 4

    # Calculate the cost of student tickets
    student_ticket_cost = num_students * 1

    # Calculate the cost of adult tickets
    adult_ticket_cost = num_teachers * 3

    # Calculate the total cost of museum tickets
    total_cost = student_ticket_cost + adult_ticket_cost
    result = total_cost
    return result

print(solution())