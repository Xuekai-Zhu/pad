def solution():
    # Calculate the potential revenue lost by the "Surprise" shop during the 3 days of Christmas holidays each year
    potential_revenue_lost_per_year = 5 * 3  # $5,000 lost each day when the shop is closed

    # Calculate the potential revenue lost by the "Surprise" shop during 6 years of activity
    potential_revenue_lost_in_six_years = potential_revenue_lost_per_year * 6

    result = potential_revenue_lost_in_six_years
    return result

print(solution())