def solution():
    student_tickets = 20
    adult_tickets = 12
    student_ticket_price = 6
    adult_ticket_price = 8

    # Calculate the total revenue from student tickets
    student_ticket_revenue = student_tickets * student_ticket_price

    # Calculate the total revenue from adult tickets
    adult_ticket_revenue = adult_tickets * adult_ticket_price

    # Calculate the total revenue from all tickets
    total_revenue = student_ticket_revenue + adult_ticket_revenue
    result = total_revenue
    return result

print(solution())