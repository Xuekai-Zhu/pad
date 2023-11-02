def solution():
    bikes_added_per_week = 3  # The owner adds 3 bikes to her stock every week
    bikes_sold_in_a_month = 18  # The owner sold 18 bikes in a month
    bikes_remaining_in_stock = 45  # The owner had 45 bikes remaining in stock after a month

    # Calculate the number of weeks in a month
    weeks_in_a_month = 4

    # Calculate the number of bikes the owner had originally
    original_stock = bikes_remaining_in_stock - (weeks_in_a_month * bikes_added_per_week) + bikes_sold_in_a_month
    result = original_stock
    return result

print(solution())