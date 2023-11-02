def solution():
    hourly_rate = 12  # Each employee is paid $12 per hour
    hours_per_day = 10  # Employees work 10 hours per day
    days_per_week = 5  # Employees work 5 days per week
    weeks_per_month = 4  # There are 4 weeks in a month
    initial_employees = 500  # There are initially 500 employees
    additional_employees = 200  # The company hires 200 more employees
    total_employees = initial_employees + additional_employees

    # Calculate the total amount the company pays its employees per month
    total_payroll = total_employees * hourly_rate * hours_per_day * days_per_week * weeks_per_month
    result = total_payroll
    return result

print(solution())