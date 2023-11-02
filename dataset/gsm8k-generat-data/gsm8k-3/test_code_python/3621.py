def solution():
    """In a car dealership, Fiona worked for 40 hours a week, John for 30 hours, and Jeremy for 25 hours. If the employees are paid $20 per hour, how much money does their boss spend paying all of them every month?"""
    # Define the hourly rate
    RATE = 20

    # Calculate the total pay for each employee
    fiona_pay = 40 * RATE
    john_pay = 30 * RATE
    jeremy_pay = 25 * RATE

    # Calculate the total pay for all employees
    total_pay = fiona_pay + john_pay + jeremy_pay

    # Display the total pay
    result = total_pay
    return result

print(solution())