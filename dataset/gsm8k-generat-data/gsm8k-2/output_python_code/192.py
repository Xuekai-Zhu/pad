def solution():
    """Apple sold 100 iPhones at their New York store today for an average cost of $1000. They also sold 20 iPads for an average cost of $900 and 80 Apple TVs for an average cost of $200. What was the average cost across all products sold today?"""
    iphone_sales = 100
    iphone_price = 1000
    ipad_sales = 20
    ipad_price = 900
    apple_tv_sales = 80
    apple_tv_price = 200
    total_sales = iphone_sales + ipad_sales + apple_tv_sales
    total_revenue = (iphone_sales * iphone_price) + (ipad_sales * ipad_price) + (apple_tv_sales * apple_tv_price)
    average_cost = total_revenue / total_sales
    result = average_cost
    return result

print(solution())