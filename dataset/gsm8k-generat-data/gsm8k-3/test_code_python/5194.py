def solution():
    """Sean designs and sells patches.  He orders his patches in a unit of 100 and is charged $1.25 per patch.  If he turns around and sells all 100 patches for $12.00 each, what is his net profit?"""
    # Define the cost and selling price of each patch
    COST_PER_PATCH = 1.25
    SELLING_PRICE_PER_PATCH = 12.00

    # Determine the profit per patch
    profit_per_patch = SELLING_PRICE_PER_PATCH - COST_PER_PATCH

    # Calculate the net profit for 100 patches
    net_profit = profit_per_patch * 100

    # Display the net profit
    result = net_profit
    return result

print(solution())