def solution():
    """James opens up a flower shop. He needs to pay rent of $1200 a week with an additional 20% of rent to pay for utilities and he has 2 employees per shift with the store open 16 hours a day for 5 days a week. If he pays each employee $12.50 an hour, what are his weekly expenses to run the store?"""
    rent = 1200
    utilities = rent * 0.2
    employees_per_shift = 2
    hours_per_day = 16
    days_per_week = 5
    hourly_wage = 12.5
    weekly_wages = employees_per_shift * hours_per_day * days_per_week * hourly_wage
    total_expenses = rent + utilities + weekly_wages
    result = total_expenses
    return result

print(solution())