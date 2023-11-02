def solution():
    """In a certain company, for every customer served, an employee gets as many bonus points, as 20% of the number of customers served. On Monday, Tom served 10 customers per hour for 8 hours. How many bonus points did Tom earn that day?"""
    # Define the number of customers served per hour and the number of hours worked
    customers_per_hour = 10
    hours_worked = 8

    # Calculate the total number of customers served
    total_customers = customers_per_hour * hours_worked

    # Calculate the number of bonus points earned
    bonus_points = total_customers * 0.2

    # return the result
    result = bonus_points
    return result

print(solution())