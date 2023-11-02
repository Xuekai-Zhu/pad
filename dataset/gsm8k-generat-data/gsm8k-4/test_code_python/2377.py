def solution():
    """Tickets to the school play cost $6 for students and $8 for adults. If 20 students and 12 adults bought tickets, how many dollars' worth of tickets were sold?"""
    # Define the ticket prices and the number of students and adults
    student_price = 6
    adult_price = 8
    num_students = 20
    num_adults = 12

    # Calculate the total amount of money from student tickets and adult tickets
    student_total = student_price * num_students
    adult_total = adult_price * num_adults

    # Calculate the total amount of money from all tickets sold
    total_sales = student_total + adult_total

    # return the result
    result = total_sales
    return result

print(solution())