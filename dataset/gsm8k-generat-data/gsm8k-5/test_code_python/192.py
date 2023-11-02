def solution():
    total_sales = (100 * 1000) + (20 * 900) + (80 * 200)  # Total sales in dollars
    total_items = 100 + 20 + 80  # Total number of items sold

    # Calculate the average cost across all products sold today
    average_cost = total_sales / total_items
    result = average_cost
    return result

print(solution())