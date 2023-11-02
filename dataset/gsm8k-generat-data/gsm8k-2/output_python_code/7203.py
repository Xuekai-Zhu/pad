def solution():
    """A 4th grade class with 20 students and 3 teachers is going to a science museum. The entrance ticket costs $5 each. How much will they pay for the entrance tickets?"""
    num_students = 20
    num_teachers = 3
    ticket_price = 5
    total_tickets = num_students + num_teachers
    total_cost = total_tickets * ticket_price
    result = total_cost
    return result

print(solution())