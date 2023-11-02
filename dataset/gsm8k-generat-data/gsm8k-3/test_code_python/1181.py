def solution():
    """Mr Fletcher hired 2 men to dig a well in his compound. They worked for 10 hours on the first day, 8 hours on the second day and finished the job on the third day after working 15 hours. If Mr Fletcher paid each of them $10 per hour of work, calculate the total amount of money they received altogether?"""
    # Define the amount paid per hour of work
    PAY_PER_HOUR = 10

    # Calculate the number of hours worked by each man
    man1_hours = 10 + 8 + 15
    man2_hours = 10 + 8 + 15

    # Calculate the total amount paid to each man
    man1_pay = man1_hours * PAY_PER_HOUR
    man2_pay = man2_hours * PAY_PER_HOUR

    # Calculate the total amount paid to both men
    total_pay = man1_pay + man2_pay

    # Display the total amount paid
    result = total_pay
    return result

print(solution())