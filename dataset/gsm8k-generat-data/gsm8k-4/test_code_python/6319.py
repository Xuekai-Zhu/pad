def solution():
    """Jean needs to buy 10 new pairs of pants. A store is running a sale for 20% off. If the pants normally retail for $45 each how much will she need to pay for all of them after paying a 10% tax?"""
    # Define the parameters
    num_pants = 10
    retail_price = 45
    sale_percent = 20
    tax_percent = 10

    # Calculate the sale price per pant
    sale_price = retail_price - (retail_price * sale_percent / 100)

    # Calculate the total cost before tax
    total_cost_before_tax = num_pants * sale_price

    # Calculate the amount of tax
    tax_amount = total_cost_before_tax * tax_percent / 100

    # Calculate the total cost after tax
    total_cost_after_tax = total_cost_before_tax + tax_amount

    # Return the result
    result = total_cost_after_tax
    return result

print(solution())