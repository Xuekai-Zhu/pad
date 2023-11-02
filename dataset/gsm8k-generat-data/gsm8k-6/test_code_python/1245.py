def solution():
    # Calculate the total number of watermelons Alice had
    total_watermelons = 10 * 12  # 1 dozen = 12 watermelons

    # Calculate the number of watermelons sold yesterday
    sold_yesterday = 0.4 * total_watermelons

    # Calculate the number of watermelons remaining after yesterday's sales
    remaining_watermelons = total_watermelons - sold_yesterday

    # Calculate the number of watermelons sold today
    sold_today = remaining_watermelons / 4

    # Calculate the number of watermelons left to be sold tomorrow
    left_to_sell = remaining_watermelons - sold_today

    result = left_to_sell
    return result

print(solution())