def solution():
    """James opens up a flower shop. He needs to pay rent of $1200 a week with an additional 20% of rent to pay for utilities
    and he has 2 employees per shift with the store open 16 hours a day for 5 days a week.
    If he pays each employee $12.50 an hour, what are his weekly expenses to run the store?"""
    # Define the cost of rent, utilities, and number of employees
    rent = 1200
    utilities = rent * 0.2
    num_employees = 2

    # Calculate the total cost of wages for a week
    hours_per_week = 16 * 5
    wage_per_hour = 12.50
    total_wages = num_employees * hours_per_week * wage_per_hour

    # Calculate the total weekly expenses
    total_expenses = rent + utilities + total_wages

    result = total_expenses
    return result

print(solution())