def solution():
    # Calculate the total earnings of Agnes for a week
    agnes_weekly_earnings = 15 * 8

    # Calculate Agnes' monthly earnings
    agnes_monthly_earnings = agnes_weekly_earnings * 4

    # Calculate how many hours Mila needs to work to earn the same amount
    mila_hourly_earnings = 10
    mila_hours_needed = agnes_monthly_earnings / mila_hourly_earnings
    result = mila_hours_needed
    return result

print(solution())