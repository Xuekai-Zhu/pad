def solution():
    """On Thursday Walmart sold 210 pounds of ground beef. On Friday they sold twice that amount. On Saturday they only sold 150 pounds. What was the average amount of beef sold per day?"""
    thursday_sales = 210
    friday_sales = 2 * thursday_sales
    saturday_sales = 150
    total_sales = thursday_sales + friday_sales + saturday_sales
    average_sales_per_day = total_sales / 3
    result = average_sales_per_day
    return result

print(solution())