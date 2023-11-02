def solution():
    """12 archeology students and 4 teachers went on a field trip to a dinosaur museum. Student tickets cost $1 each, and adult tickets cost $3 each. How much did the museum tickets cost in all?"""
    num_students = 12
    num_teachers = 4
    student_ticket_cost = 1
    teacher_ticket_cost = 3
    total_cost = num_students * student_ticket_cost + num_teachers * teacher_ticket_cost
    result = total_cost
    return result

print(solution())