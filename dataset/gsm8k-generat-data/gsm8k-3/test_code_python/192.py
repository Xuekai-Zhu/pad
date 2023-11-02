def solution():
    """Apple sold 100 iPhones at their New York store today for an average cost of $1000.
    They also sold 20 iPads for an average cost of $900 and 80 Apple TVs for an average cost of $200.
    What was the average cost across all products sold today?"""
    
    # Define the number of units sold and their respective average cost
    iphone_units = 100
    iphone_cost = 1000
    ipad_units = 20
    ipad_cost = 900
    appletv_units = 80
    appletv_cost = 200
    
    # Calculate the total revenue and total number of units sold
    total_revenue = (iphone_units * iphone_cost) + (ipad_units * ipad_cost) + (appletv_units * appletv_cost)
    total_units = iphone_units + ipad_units + appletv_units
    
    # Calculate the average cost across all products sold today
    avg_cost = total_revenue / total_units
    
    # Return the result
    result = avg_cost
    return result

print(solution())