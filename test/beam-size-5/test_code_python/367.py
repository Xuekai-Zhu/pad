def solution():
    
    # Define the number of shoes sold on Friday
    friday_sales = 14

    # Calculate the number of shoes sold on the second day
    day2_sales = friday_sales * 2

    # Calculate the number of shoes sold on the third day
    day3_sales = day2_sales / 2

    # Calculate the total number of shoes sold by the end of the sale
    total_sales = friday_sales + day2_sales + day3_sales

    # Display the total number of shoes sold
    result = total_sales
    return result

print(solution())