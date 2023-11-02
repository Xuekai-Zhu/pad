def solution():
    """Sara is checking out two different stores to buy a computer. The first store offers a device for $950 with a 6% discount. The second sells the same computer for €920 with a 5% discount. What is the difference in price between the two stores?"""
    # Define the original prices of the computers
    price1 = 950
    price2 = 920
    
    # Calculate the prices after discounts
    price1_discounted = price1 * 0.94
    price2_discounted = price2 * 0.95
    
    # Calculate the difference in prices
    price_difference = abs(price1_discounted - price2_discounted)
    
    # Return the result
    result = price_difference
    return result

print(solution())