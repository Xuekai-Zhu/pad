def solution():
    """Alice had 10 dozens of watermelons. She sold 40% of it yesterday and 1/4 of the remaining today, How many watermelons are left to be sold tomorrow?"""
    # Define the initial number of watermelons
    initial_watermelons = 10 * 12

    # Calculate the number of watermelons sold yesterday
    sold_yesterday = 0.4 * initial_watermelons

    # Calculate the number of watermelons remaining after yesterday's sales
    remaining = initial_watermelons - sold_yesterday

    # Calculate the number of watermelons sold today
    sold_today = 0.25 * remaining

    # Calculate the number of watermelons left to be sold tomorrow
    left_tomorrow = remaining - sold_today

    # Display the number of watermelons left to be sold tomorrow
    result = left_tomorrow
    return result

print(solution())