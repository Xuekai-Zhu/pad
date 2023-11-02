def solution():
    amazon_boots_cost = 16
    amazon_shipping_cost = 4
    ebay_boots_cost = 13
    ebay_shipping_cost = 2 * amazon_boots_cost

    # Calculate the total cost of all boots on Amazon.com
    total_amazon_boots_cost = amazon_boots_cost + amazon_shipping_cost

    # Calculate the total cost of all boots on eBay
    total_ebay_boots_cost = ebay_boots_cost + ebay_shipping_cost

    # Calculate the difference in cost between eBay and Amazon.com
    cost_difference = total_ebay_boots_cost - total_amazon_boots_cost
    result = cost_difference
    return result

print(solution())