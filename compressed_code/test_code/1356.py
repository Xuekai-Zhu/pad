def solution():
    
    agnes_weekly_earnings = 15 * 8
    monthly_earnings_agnes = agnes_weekly_earnings * 4
    hourly_rate_mila = 10
    hours_needed_mila = monthly_earnings_agnes / hourly_rate_mila
    result = hours_needed_mila
    return result

print(solution())