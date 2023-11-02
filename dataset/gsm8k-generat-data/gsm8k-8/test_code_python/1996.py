def solution():
    # Define the number of flowers sold on each day
    monday_sales = 4
    tuesday_sales = 8
    friday_sales = 2 * monday_sales

    # Calculate the total number of flowers sold
    total_sales = monday_sales + tuesday_sales + friday_sales
    result = total_sales
    return result

print(solution())