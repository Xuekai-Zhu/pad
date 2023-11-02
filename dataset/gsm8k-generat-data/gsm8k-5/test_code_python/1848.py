def solution():
    # Number of bouquets sold on Monday
    monday_sales = 12

    # Number of bouquets sold on Tuesday (3 times Monday's sales)
    tuesday_sales = monday_sales * 3

    # Number of bouquets sold on Wednesday (1/3 of Tuesday's sales)
    wednesday_sales = tuesday_sales / 3

    # Total number of bouquets sold during the three-day sale
    total_sales = monday_sales + tuesday_sales + wednesday_sales
    result = total_sales
    return result

print(solution())