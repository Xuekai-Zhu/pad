def solution():
    """Alice had 10 dozens of watermelons. She sold 40% of it yesterday and 1/4 of the remaining today, How many watermelons are left to be sold tomorrow?"""
    total_watermelons = 10 * 12  # converting dozens to individual watermelons
    yesterday_sold = total_watermelons * 0.4
    remaining_watermelons = total_watermelons - yesterday_sold
    today_sold = remaining_watermelons / 4
    left_to_sell = remaining_watermelons - today_sold
    result = left_to_sell
    return result

print(solution())