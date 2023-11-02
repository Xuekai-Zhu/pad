def solution():
    """Hillary always buys the Wednesday, Thursday and Friday editions of the local newspaper for $0.50 each. On Sunday, she spends $2.00 to get that copy. How much does she spend on the newspaper over 8 weeks?"""
    weekday_price = 0.5 * 3
    sunday_price = 2
    total_price_per_week = weekday_price + sunday_price
    total_price_over_8_weeks = total_price_per_week * 8
    result = total_price_over_8_weeks
    return result

print(solution())