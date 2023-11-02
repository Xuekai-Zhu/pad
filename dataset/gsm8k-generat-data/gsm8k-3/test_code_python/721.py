def solution():
    """An electronic shop offers smartphones for $300 each, personal computers for $500 more than smartphones, and advanced tablets for the sum of the prices of a smartphone and personal computer. How much do you have to pay to buy one of each of the three mentioned products?"""
    # Define the prices of each product
    smartphone_price = 300
    computer_price = smartphone_price + 500
    tablet_price = smartphone_price + computer_price

    # Calculate the total cost of all three products
    total_cost = smartphone_price + computer_price + tablet_price

    # Display the total cost
    result = total_cost
    return result

print(solution())