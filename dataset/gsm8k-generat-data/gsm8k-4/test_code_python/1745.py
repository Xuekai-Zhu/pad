def solution():
    """There are two babysitters named Mila and Agnes. Mila makes $10 an hour while Agnes makes $15 an hour. Agnes works 8 hours each week. How many hours does Mila need to work to earn as much as Agnes in a month?"""
    # Define the hourly rates for Mila and Agnes
    mila_rate = 10
    agnes_rate = 15

    # Calculate the weekly earnings for Agnes
    agnes_weekly_earnings = agnes_rate * 8

    # Calculate the monthly earnings for Agnes
    agnes_monthly_earnings = agnes_weekly_earnings * 4

    # Calculate the hourly rate for Mila needed to earn the same as Agnes in a month
    mila_monthly_rate = agnes_monthly_earnings / (4 * 4)  # 4 weeks, 4 hours a week

    # Calculate the number of hours Mila needs to work to earn as much as Agnes in a month
    mila_hours = agnes_monthly_earnings / mila_monthly_rate

    result = round(mila_hours)
    return result

print(solution())