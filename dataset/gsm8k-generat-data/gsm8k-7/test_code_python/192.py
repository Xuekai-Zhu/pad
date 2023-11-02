def solution():
    num_iPhones = 100
    iPhone_price = 1000

    num_iPads = 20
    iPad_price = 900

    num_Apple_TVs = 80
    Apple_TV_price = 200

    # Calculate the total revenue from iPhone sales
    total_iPhone_revenue = num_iPhones * iPhone_price

    # Calculate the total revenue from iPad sales
    total_iPad_revenue = num_iPads * iPad_price

    # Calculate the total revenue from Apple TV sales
    total_Apple_TV_revenue = num_Apple_TVs * Apple_TV_price

    # Calculate the total revenue from all products sold
    total_revenue = total_iPhone_revenue + total_iPad_revenue + total_Apple_TV_revenue

    # Calculate the total number of products sold
    total_num_products = num_iPhones + num_iPads + num_Apple_TVs

    # Calculate the average cost across all products sold
    avg_cost = total_revenue / total_num_products
    result = avg_cost
    return result

print(solution())