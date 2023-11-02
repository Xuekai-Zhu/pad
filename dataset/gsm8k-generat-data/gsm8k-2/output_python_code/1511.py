def solution():
    """In a certain company, for every customer served, an employee gets as many bonus points, as 20% of the number of customers served. On Monday, Tom served 10 customers per hour for 8 hours. How many bonus points did Tom earn that day?"""
    customers_per_hour = 10
    hours_worked = 8
    total_customers = customers_per_hour * hours_worked
    bonus_percentage = 0.2
    bonus_points = bonus_percentage * total_customers
    result = bonus_points
    return result

print(solution())