def solution():
    """Tickets to the school play cost $6 for students and $8 for adults. If 20 students and 12 adults bought tickets, how many dollars' worth of tickets were sold?"""
    # Define the ticket prices
    STUDENT_PRICE = 6
    ADULT_PRICE = 8

    # Define the number of students and adults who bought tickets
    num_students = 20
    num_adults = 12

    # Calculate the total sales from student tickets
    student_sales = num_students * STUDENT_PRICE

    # Calculate the total sales from adult tickets
    adult_sales = num_adults * ADULT_PRICE

    # Calculate the total sales from all tickets
    total_sales = student_sales + adult_sales

    # Display the total sales
    result = total_sales
    return result

print(solution())