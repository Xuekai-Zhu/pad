def solution():
    num_students = 12  # 12 archeology students
    num_teachers = 4  # 4 teachers
    student_ticket_cost = 1  # $1 per student ticket
    adult_ticket_cost = 3  # $3 per adult ticket

    # Calculate the total cost of student tickets
    student_ticket_total = num_students * student_ticket_cost

    # Calculate the total cost of adult tickets
    adult_ticket_total = num_teachers * adult_ticket_cost

    # Calculate the total cost of all tickets
    total_cost = student_ticket_total + adult_ticket_total
    result = total_cost
    return result

print(solution())