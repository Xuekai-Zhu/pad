def solution():
    good_week_sales = 2 * 800  # Double the sales on a tough week
    tough_week_sales = 800
    num_good_weeks = 5
    num_tough_weeks = 3

    # Calculate the total sales for all good weeks
    total_good_week_sales = num_good_weeks * good_week_sales

    # Calculate the total sales for all tough weeks
    total_tough_week_sales = num_tough_weeks * tough_week_sales

    # Calculate the total sales for all weeks
    total_sales = total_good_week_sales + total_tough_week_sales
    result = total_sales
    return result

print(solution())