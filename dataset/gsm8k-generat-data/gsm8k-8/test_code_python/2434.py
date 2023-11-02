def solution():
    # Define the number of boxes sold on Friday
    friday_sales = 40

    # Define the number of boxes sold on Saturday
    saturday_sales = 2 * friday_sales - 10

    # Define the number of boxes sold on Sunday
    sunday_sales = friday_sales / 2

    # Calculate the total number of boxes sold over the three days
    total_sales = friday_sales + saturday_sales + sunday_sales
    result = total_sales
    return result

print(solution())