def solution():
    # Calculate the earnings for the first month
    earnings_first_month = 10 * 30

    # Calculate the earnings for the second month
    earnings_second_month = 2 * earnings_first_month

    # Calculate the earnings for the third month
    earnings_third_month = earnings_second_month
    earnings_third_month_every_other_day = earnings_second_month / 2  # She works every other day in the third month
    earnings_third_month = earnings_third_month_every_other_day * 15  # 15 days in the third month

    # Calculate the total earnings for all three months
    total_earnings = earnings_first_month + earnings_second_month + earnings_third_month
    result = total_earnings
    return result

print(solution())