def solution():
    """Walter works 5 days a week in a fast-food chain and earns $5 per hour. Since he is a working student, he can only work 4 hours a day and allocates 3/4 of his weekly earning for his schooling. How much does he allocate for school?"""
    days_per_week = 5
    hours_per_day = 4
    hourly_rate = 5
    weekly_earnings = days_per_week * hours_per_day * hourly_rate
    allocation_proportion = 3 / 4
    allocation_amount = weekly_earnings * allocation_proportion
    result = allocation_amount
    return result

print(solution())