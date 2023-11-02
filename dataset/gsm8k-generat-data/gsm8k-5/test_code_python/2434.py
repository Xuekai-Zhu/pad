def solution():
    friday_sales = 40  # Tameka sold 40 boxes on Friday
    saturday_sales = (2 * friday_sales) - 10  # Tameka sold 10 fewer than twice Friday's sales on Saturday
    sunday_sales = friday_sales / 2  # Tameka sold half as many on Sunday as she did on Friday

    # Calculate the total number of boxes Tameka sold over the three days
    total_sales = friday_sales + saturday_sales + sunday_sales
    result = total_sales
    return result

print(solution())