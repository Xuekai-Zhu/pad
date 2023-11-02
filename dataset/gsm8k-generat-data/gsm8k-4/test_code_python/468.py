def solution():
    """A shopping center sells T-shirts at $8 each, a sweater at $18,  and a jacket at $80. The jacket is on sale with a 10% discount. The sales tax is 5%.  Kevin wants to buy six T-shirts, four sweaters, and five jackets for his children. How much does Kevin have to pay for all the items, including the sales tax?"""
    # Define the prices of the items
    tshirt_price = 8
    sweater_price = 18
    jacket_price = 80

    # Calculate the total price of the items before discount and tax
    total_price = 6 * tshirt_price + 4 * sweater_price + 5 * jacket_price

    # Apply the discount to the price of the jackets
    total_price -= 0.1 * 5 * jacket_price

    # Calculate the sales tax
    sales_tax = 0.05 * total_price

    # Calculate the total price including tax
    total_price += sales_tax

    result = total_price
    return result

print(solution())