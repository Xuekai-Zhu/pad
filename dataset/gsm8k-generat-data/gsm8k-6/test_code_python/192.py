def solution():
    total_sales = (100*1000) + (20*900) + (80*200)  # calculate the total sales
    total_items_sold = 100 + 20 + 80  # calculate the total number of products sold
    average_cost = total_sales / total_items_sold  # calculate the average cost
    result = average_cost
    return result

print(solution())