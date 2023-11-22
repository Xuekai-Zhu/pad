def solution():
    
    # Define the prices of the boots and shipping
    amazon_price = 16
    amazon_shipping = 4

    # Define the prices of the shoes and shipping
    eay_price = 13
    eay_shipping = 2 * amazon_shipping

    # Calculate the total cost of the boots on Amazon.com
    amazon_cost = amazon_price + amazon_shipping

    # Calculate the total cost of the shoes on eBay
    eay_cost = eay_price + eay_shipping

    # Calculate the difference in cost between the boots on eBay and the Amazon.com
    difference = eay_cost - amazon_cost

    # return the result
    result = difference
    return result

print(solution())