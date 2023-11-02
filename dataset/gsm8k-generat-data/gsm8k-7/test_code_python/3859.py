def solution():
    days_closed = 3
    potential_earnings_per_day = 5000
    years_of_activity = 6

    # Calculate the total potential earnings lost per year
    earnings_lost_per_year = days_closed * potential_earnings_per_day

    # Calculate the total potential earnings lost over 6 years
    total_earnings_lost = earnings_lost_per_year * years_of_activity
    result = total_earnings_lost
    return result

print(solution())