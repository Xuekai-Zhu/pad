def solution():
    """12 archeology students and 4 teachers went on a field trip to a dinosaur museum. Student tickets cost $1 each, and adult tickets cost $3 each. How much did the museum tickets cost in all?"""
    # Define the cost of a student ticket and an adult ticket
    STUDENT_TICKET_PRICE = 1
    ADULT_TICKET_PRICE = 3

    # Define the number of students and teachers
    num_students = 12
    num_teachers = 4

    # Calculate the total cost of the student tickets
    student_cost = num_students * STUDENT_TICKET_PRICE

    # Calculate the total cost of the adult tickets
    adult_cost = num_teachers * ADULT_TICKET_PRICE

    # Calculate the total cost of all the tickets
    total_cost = student_cost + adult_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())