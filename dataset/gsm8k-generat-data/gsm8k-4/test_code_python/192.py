def solution():
    """Apple sold 100 iPhones at their New York store today for an average cost of $1000. They also sold 20 iPads for an average cost of $900 and 80 Apple TVs for an average cost of $200. What was the average cost across all products sold today?"""
    # Define the number and cost of each product sold
    iphone_number = 100
    iphone_cost = 1000
    ipad_number = 20
    ipad_cost = 900
    appletv_number = 80
    appletv_cost = 200

    # Calculate the total revenue and number of products sold
    total_revenue = (iphone_number * iphone_cost) + (ipad_number * ipad_cost) + (appletv_number * appletv_cost)
    total_products = iphone_number + ipad_number + appletv_number

    # Calculate the average cost across all products sold
    average_cost = total_revenue / total_products

    # return the result
    result = average_cost
    return result

print(solution())