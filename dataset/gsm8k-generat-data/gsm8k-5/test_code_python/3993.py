def solution():
    rent = 1200  # James pays $1200 a week for rent
    utilities = rent * 0.2  # James pays 20% of the rent for utilities
    employees_per_shift = 2  # James has 2 employees per shift
    store_open_hours_per_week = 16 * 5  # The store is open 16 hours a day for 5 days a week
    hourly_employee_wage = 12.5  # James pays each employee $12.50 an hour

    # Calculate the total weekly wages for employees
    weekly_wages = employees_per_shift * hourly_employee_wage * (store_open_hours_per_week / 8)

    # Calculate the total weekly expenses
    total_expenses = rent + utilities + weekly_wages
    result = total_expenses
    return result

print(solution())