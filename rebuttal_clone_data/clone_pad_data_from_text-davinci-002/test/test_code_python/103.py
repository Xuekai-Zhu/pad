def solution():
    
    iPhones_sold = 100
    iPads_sold = 20
    Apple_TVs_sold = 80
    iPhone_average_cost = 1000
    iPad_average_cost = 900
    Apple_TV_average_cost = 200
    total_products_sold = iPhones_sold + iPads_sold + Apple_TVs_sold
    total_revenue = (iPhones_sold * iPhone_average_cost) + (iPads_sold * iPad_average_cost) + (Apple_TVs_sold * Apple_TV_average_cost)
    average_cost = total_revenue / total_products_sold
    result = average_cost
    
    return result

print(solution())