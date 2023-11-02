def solution():
    """A convenience store sold 100 bags of chips in a month. In the first week, 15 bags of chips were sold. In the second week, thrice as many bags of chips were sold. There was an equal number of chips sold in the third and fourth week. How many chips was each sold in the third and fourth week?"""
    total_bags = 100
    first_week_sales = 15
    second_week_sales = first_week_sales * 3
    remaining_bags = total_bags - first_week_sales - second_week_sales
    third_week_sales = fourth_week_sales = remaining_bags / 2
    result = (third_week_sales, fourth_week_sales)
    return result

print(solution())