def solution():
    
    # Define the number of shoes sold on each day
    friday_sales = 14
    saturday_sales = friday_sales * 2
    last_day_sales = saturday_sales / 2
    total_sales = friday_sales + saturday_sales + last_day_sales

    # Display the total number of shoes sold
    result = total_sales
    return result

print(solution())