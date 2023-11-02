def solution():
    """Tickets to the school play cost $6 for students and $8 for adults. If 20 students and 12 adults bought tickets, how many dollars' worth of tickets were sold?"""
    student_tickets = 20
    adult_tickets = 12
    student_price = 6
    adult_price = 8
    total_sales = student_tickets * student_price + adult_tickets * adult_price
    result = total_sales
    return result

print(solution())