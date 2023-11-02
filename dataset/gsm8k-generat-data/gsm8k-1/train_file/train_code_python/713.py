def solution():
    """John runs a website that gets 30000 visits a month, for a normal 30 day month. He gets $.01 per visit. How much does he make per day?"""
    visits_per_month = 30000
    days_per_month = 30
    revenue_per_visit = 0.01
    total_revenue_per_month = visits_per_month * revenue_per_visit
    revenue_per_day = total_revenue_per_month / days_per_month
    result = revenue_per_day
    return result

print(solution())