def solution():
    # Define the number of marigolds sold each day
    day1_sales = 14
    day2_sales = day1_sales + 25
    day3_sales = 2 * day2_sales

    # Calculate the total number of marigolds sold
    total_sales = day1_sales + day2_sales + day3_sales
    result = total_sales
    return result

print(solution())