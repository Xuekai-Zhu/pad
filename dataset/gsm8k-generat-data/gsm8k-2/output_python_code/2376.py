def solution():
    """Tickets to the school play cost $6 for students and $8 for adults. If 20 students and 12 adults bought tickets, how many dollars' worth of tickets were sold?"""
    student_price = 6
    adult_price = 8
    student_count = 20
    adult_count = 12
    total_sales = (student_price * student_count) + (adult_price * adult_count)
    result = total_sales
    return result

print(solution())