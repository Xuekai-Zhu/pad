def solution():
    total_bags_sold = 100  # The store sold 100 bags of chips in a month
    first_week_sales = 15  # 15 bags of chips were sold in the first week
    second_week_sales = 3 * first_week_sales  # In the second week, thrice as many bags were sold as in the first week
    remaining_sales = total_bags_sold - first_week_sales - second_week_sales # Sales remaining for the last two weeks
    third_week_sales = remaining_sales / 2  # The third and fourth week sales were equal
    fourth_week_sales = third_week_sales
    
    result = (third_week_sales, fourth_week_sales)
    return result

print(solution())