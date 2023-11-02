def solution():
    """12 archeology students and 4 teachers went on a field trip to a dinosaur museum. Student tickets cost $1 each, and adult tickets cost $3 each. How much did the museum tickets cost in all?"""
    # Define the number of students and teachers
    num_students = 12
    num_teachers = 4

    # Calculate the cost of student tickets
    student_ticket_cost = num_students * 1

    # Calculate the cost of teacher tickets
    teacher_ticket_cost = num_teachers * 3

    # Calculate the total cost of the museum tickets
    total_cost = student_ticket_cost + teacher_ticket_cost

    # return the result
    result = total_cost
    return result

print(solution())