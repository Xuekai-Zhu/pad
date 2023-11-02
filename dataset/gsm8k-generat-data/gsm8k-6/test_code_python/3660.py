def solution():
    # Calculate the total sales needed to make a $200 profit
    total_sales_needed = (200 / 0.2)  # expenses are 80% of total sales, so profit is 20% of total sales
    # Calculate the number of ice cream cones needed to reach the total sales
    cones_needed = total_sales_needed / 5  # each ice cream cone is $5
    result = cones_needed
    return result

print(solution())