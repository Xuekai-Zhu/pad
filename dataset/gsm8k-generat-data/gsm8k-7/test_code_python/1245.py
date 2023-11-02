def solution():
    num_watermelons = 10 * 12  # Convert dozens to individual watermelons
    sold_yesterday_percent = 0.4
    sold_today_fraction = 1/4

    # Calculate the number of watermelons sold yesterday
    num_sold_yesterday = int(num_watermelons * sold_yesterday_percent)

    # Calculate the number of watermelons remaining after yesterday's sales
    num_remaining = num_watermelons - num_sold_yesterday

    # Calculate the number of watermelons sold today
    num_sold_today = int(num_remaining * sold_today_fraction)

    # Calculate the number of watermelons remaining for tomorrow's sales
    num_remaining_tomorrow = num_remaining - num_sold_today
    result = num_remaining_tomorrow
    return result

print(solution())