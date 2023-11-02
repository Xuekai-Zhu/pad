def solution():
    
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