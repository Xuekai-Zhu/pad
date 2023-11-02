def solution():
    """Alice had 10 dozens of watermelons. She sold 40% of it yesterday and 1/4 of the remaining today, How many watermelons are left to be sold tomorrow?"""
    # Define the initial number of watermelons
    initial_watermelons = 10 * 12

    # Calculate the number of watermelons sold yesterday
    sold_yesterday = initial_watermelons * 0.4

    # Calculate the number of watermelons remaining after yesterday's sales
    remaining_watermelons = initial_watermelons - sold_yesterday

    # Calculate the number of watermelons sold today
    sold_today = remaining_watermelons * (1/4)

    # Calculate the number of watermelons remaining after today's sales
    remaining_tomorrow = remaining_watermelons - sold_today

    result = remaining_tomorrow
    return result

print(solution())