def solution():
    """Sean designs and sells patches. He orders his patches in a unit of 100 and is charged $1.25 per patch. If he turns around and sells all 100 patches for $12.00 each, what is his net profit?"""
    
    # Define the cost per patch and the selling price per patch
    cost_per_patch = 1.25
    selling_price_per_patch = 12.00

    # Calculate the total cost of 100 patches
    total_cost = cost_per_patch * 100

    # Calculate the total revenue from selling 100 patches
    total_revenue = selling_price_per_patch * 100

    # Calculate the net profit
    net_profit = total_revenue - total_cost

    # return the result
    result = net_profit
    return result

print(solution())