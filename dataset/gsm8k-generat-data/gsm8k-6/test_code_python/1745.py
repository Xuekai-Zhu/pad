def solution():
    # Calculate the total amount earned by Agnes in a week
    agnes_weekly_earnings = 15 * 8  # Agnes makes $15 an hour and works 8 hours each week

    # Calculate the total amount earned by Agnes in a month
    agnes_monthly_earnings = agnes_weekly_earnings * 4  # assuming 4 weeks in a month

    # Calculate the number of hours Mila needs to work to earn the same amount as Agnes in a month
    mila_hourly_rate = 10
    mila_hours_needed = agnes_monthly_earnings / mila_hourly_rate
    result = mila_hours_needed
    return result

print(solution())