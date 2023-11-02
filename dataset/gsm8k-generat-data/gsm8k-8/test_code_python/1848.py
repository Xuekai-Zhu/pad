def solution():
    # Calculate the number of bouquets sold on Tuesday
    tuesday_sales = 12 * 3

    # Calculate the number of bouquets sold on Wednesday
    wednesday_sales = tuesday_sales // 3

    # Calculate the total number of bouquets sold during the three day sale
    total_sales = 12 + tuesday_sales + wednesday_sales
    result = total_sales
    return result

print(solution())