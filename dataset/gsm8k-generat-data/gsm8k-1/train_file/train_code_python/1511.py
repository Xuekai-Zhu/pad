def solution():
    """In a certain company, for every customer served, an employee gets as many bonus points, as 20% of the number of customers served. On Monday, Tom served 10 customers per hour for 8 hours. How many bonus points did Tom earn that day?"""
    customers_served = 10
    hours_worked = 8
    bonus_percentage = 0.2
    bonus_points_per_customer = customers_served * bonus_percentage
    total_customers_served = customers_served * hours_worked
    total_bonus_points = total_customers_served * bonus_points_per_customer
    result = total_bonus_points
    return result

print(solution())