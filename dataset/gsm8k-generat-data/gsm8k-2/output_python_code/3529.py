def solution():
    """Walter works 5 days a week in a fast-food chain and earns $5 per hour. Since he is a working student, he can only work 4 hours a day and allocates 3/4 of his weekly earning for his schooling. How much does he allocate for school?"""
    days_per_week = 5
    hours_per_day = 4
    wage_per_hour = 5
    total_hours = days_per_week * hours_per_day
    weekly_earning = total_hours * wage_per_hour
    school_allocation = 0.75 * weekly_earning
    result = school_allocation
    return result

print(solution())