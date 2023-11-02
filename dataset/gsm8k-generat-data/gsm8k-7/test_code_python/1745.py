def solution():
    mila_rate = 10
    agnes_rate = 15
    agnes_hours = 8
    weeks_in_month = 4

    # Calculate Agnes' monthly earnings
    agnes_monthly_earnings = agnes_rate * agnes_hours * weeks_in_month

    # Calculate how many hours Mila needs to work to earn the same as Agnes
    mila_hours = agnes_monthly_earnings / mila_rate
    result = mila_hours
    return result

print(solution())