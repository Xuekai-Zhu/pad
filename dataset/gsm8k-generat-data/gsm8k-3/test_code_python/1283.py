def solution():
    """Dan spent an hour doing 400 work tasks at $0.25 each. Then Dan spent an hour doing 5 work tasks at $2.00 each. How much more did Dan make doing the good work compared to the lower-paid work?"""
    # Calculate the total amount made from the 400 tasks at $0.25 each
    task1_pay = 400 * 0.25

    # Calculate the total amount made from the 5 tasks at $2.00 each
    task2_pay = 5 * 2.00

    # Calculate the difference in pay between the two tasks
    pay_difference = task2_pay - task1_pay

    # Display the pay difference
    result = pay_difference
    return result

print(solution())