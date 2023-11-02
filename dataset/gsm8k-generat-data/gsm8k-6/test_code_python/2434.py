def solution():
    # Calculate the total number of boxes sold by Tameka over the three days
    friday_sales = 40
    saturday_sales = (2 * friday_sales) - 10  # sold 10 fewer than twice the number sold on Friday
    sunday_sales = friday_sales / 2  # sold half as many as Friday
    total_sales = friday_sales + saturday_sales + sunday_sales
    result = total_sales
    return result

print(solution())