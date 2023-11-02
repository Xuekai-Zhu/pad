def solution():
    # Define the number of boxes sold on Saturday and Sunday
    saturday_sales = 60
    sunday_sales = 1.5 * saturday_sales

    # Calculate the total number of boxes sold
    total_sales = saturday_sales + sunday_sales
    result = total_sales
    return result

print(solution())