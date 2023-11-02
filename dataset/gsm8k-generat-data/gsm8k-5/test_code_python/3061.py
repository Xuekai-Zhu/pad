def solution():
    # Calculate Mikaela's earnings in the first month
    earnings_first_month = 10 * 35  # $10 per hour, 35 hours in the first month

    # Calculate Mikaela's earnings in the second month
    earnings_second_month = 10 * 40  # $10 per hour, 5 more hours than the first month

    # Calculate total earnings
    total_earnings = earnings_first_month + earnings_second_month

    # Calculate how much Mikaela spent on her personal needs
    personal_needs = total_earnings * (4/5)

    # Calculate how much Mikaela saved
    saved_money = total_earnings - personal_needs
    result = saved_money
    return result

print(solution())