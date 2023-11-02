def solution():
    # Define the number and cost of each product
    iPhones_sold = 100
    iPhone_cost = 1000
    iPads_sold = 20
    iPad_cost = 900
    AppleTVs_sold = 80
    AppleTV_cost = 200

    # Calculate the total revenue for each product and the overall revenue
    iPhone_revenue = iPhones_sold * iPhone_cost
    iPad_revenue = iPads_sold * iPad_cost
    AppleTV_revenue = AppleTVs_sold * AppleTV_cost
    total_revenue = iPhone_revenue + iPad_revenue + AppleTV_revenue

    # Calculate the total number of products sold
    total_products_sold = iPhones_sold + iPads_sold + AppleTVs_sold

    # Calculate the average cost across all products sold
    average_cost = total_revenue / total_products_sold
    result = average_cost
    return result

print(solution())