def solution():
    """An electronic shop offers smartphones for $300 each, personal computers for $500 more than smartphones, and advanced tablets for the sum of the prices of a smartphone and personal computer. How much do you have to pay to buy one of each of the three mentioned products?"""
    # Define the prices of the products
    smartphone_price = 300
    laptop_price = smartphone_price + 500
    tablet_price = smartphone_price + laptop_price

    # Calculate the total cost of buying one of each product
    total_cost = smartphone_price + laptop_price + tablet_price

    # return the result
    result = total_cost
    return result

print(solution())