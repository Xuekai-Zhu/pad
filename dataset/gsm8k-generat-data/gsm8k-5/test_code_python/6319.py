def solution():
    num_pants = 10  # Jean needs to buy 10 pairs of pants
    retail_price = 45  # The pants normally retail for $45 each
    discount_rate = 0.2  # The store is running a sale for 20% off
    sale_price = retail_price * (1 - discount_rate)  # Calculate the sale price of each pair of pants
    pre_tax_price = num_pants * sale_price  # Calculate the total price before tax
    tax_rate = 0.1  # Jean has to pay a 10% tax
    total_price = pre_tax_price * (1 + tax_rate)  # Calculate the total price after tax
    result = total_price
    return result

print(solution())