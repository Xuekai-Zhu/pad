def solution():
    """James bought a gallon of milk for $3, a bunch of bananas for $2, and paid 20% sales tax. How much money did James spend?"""
    # Define the prices of the milk and bananas
    milk_price = 3
    bananas_price = 2

    # Calculate the sales tax
    sales_tax = 0.2

    # Calculate the total cost before tax
    total_cost_before_tax = milk_price + bananas_price

    # Calculate the total cost after tax
    total_cost_after_tax = total_cost_before_tax + (total_cost_before_tax * sales_tax)

    # Return the result
    result = total_cost_after_tax
    return result

print(solution())