def solution():
    """In a certain company, for every customer served, an employee gets as many bonus points, as 20% of the number of customers served. On Monday, Tom served 10 customers per hour for 8 hours. How many bonus points did Tom earn that day?"""
    # Define the bonus points percentage
    BONUS_PERCENTAGE = 0.2

    # Calculate the number of customers served
    customers_served = 10 * 8

    # Calculate the bonus points earned
    bonus_points = customers_served * BONUS_PERCENTAGE

    # Display the bonus points earned
    result = bonus_points
    return result

print(solution())