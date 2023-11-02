def solution():
    """In a car dealership, Fiona worked for 40 hours a week, John for 30 hours, and Jeremy for 25 hours. If the employees are paid $20 per hour, how much money does their boss spend paying all of them every month?"""
    # Define the hourly wage
    hourly_wage = 20

    # Calculate the total payment for Fiona
    fiona_payment = 40 * hourly_wage

    # Calculate the total payment for John
    john_payment = 30 * hourly_wage

    # Calculate the total payment for Jeremy
    jeremy_payment = 25 * hourly_wage

    # Calculate the total payment for all employees
    total_payment = fiona_payment + john_payment + jeremy_payment

    result = total_payment
    return result

print(solution())