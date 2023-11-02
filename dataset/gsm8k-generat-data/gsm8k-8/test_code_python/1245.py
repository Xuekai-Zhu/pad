def solution():
    # Define the number of dozens of watermelons Alice had
    total_dozens = 10

    # Calculate the total number of watermelons
    total_watermelons = total_dozens * 12

    # Calculate the number of watermelons sold yesterday
    sold_yesterday = 0.4 * total_watermelons

    # Calculate the number of watermelons remaining today
    remaining_today = total_watermelons - sold_yesterday

    # Calculate the number of watermelons sold today
    sold_today = 0.25 * remaining_today

    # Calculate the number of watermelons left to be sold tomorrow
    left_to_be_sold = remaining_today - sold_today

    result = left_to_be_sold
    return result

print(solution())