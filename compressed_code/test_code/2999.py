def solution():
    """During the Christmas holidays, all shops are closed for 3 days. During each day during this time, a shop called "Surprise" could have earned 5 thousand dollars. How much potential revenue did the "Surprise" shop lose during 6 years of activity?"""
    days_closed = 3
    revenue_lost_per_day = 5000
    years_active = 6
    total_revenue_lost = days_closed * revenue_lost_per_day * 6
    result = total_revenue_lost
    return result

print(solution())