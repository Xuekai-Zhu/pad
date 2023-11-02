def solution():
    """A company has 500 employees, each paid $12 per hour, working 10 hours a day, five days a week, 4 weeks a month. In August, the amount of work increased, and the company hired 200 more people. How much money does the company pay in total per month after the new hires?"""
    # Define the number of employees and their hourly rate
    employees = 700
    hourly_rate = 12

    # Define the number of hours worked per day, days worked per week, and weeks worked per month
    hours_per_day = 10
    days_per_week = 5
    weeks_per_month = 4

    # Calculate the total number of hours worked per month
    total_hours = employees * hours_per_day * days_per_week * weeks_per_month

    # Calculate the total cost of paying all the employees
    total_cost = total_hours * hourly_rate

    # Display the total cost
    result = total_cost
    return result

print(solution())