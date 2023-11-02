def solution():
    hourly_raise = 0.5
    weekly_hours = 40
    rent_assistance_reduction = 60

    # Calculate Bob's increased hourly rate
    new_hourly_rate = hourly_raise + 10

    # Calculate Bob's increased weekly earnings
    new_weekly_earnings = new_hourly_rate * weekly_hours

    # Calculate how much less Bob will receive in housing assistance per week
    rent_assistance_loss_per_week = rent_assistance_reduction / 4

    # Calculate how much more Bob will actually earn per week
    net_weekly_income_increase = new_weekly_earnings - rent_assistance_loss_per_week
    result = net_weekly_income_increase
    return result

print(solution())