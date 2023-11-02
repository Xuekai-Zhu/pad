def solution():
    days_closed = 3  # The shop is closed for 3 days during Christmas holidays
    potential_revenue_per_day = 5000  # The shop could have earned 5000 dollars per day

    # Calculate the potential revenue lost during 6 years of activity
    potential_revenue_lost = days_closed * potential_revenue_per_day * 6 * 2  # 6 years means 12 Christmas holidays

    result = potential_revenue_lost
    return result

print(solution())