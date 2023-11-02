def solution():
    """John needs to replace his shoes so he decides to buy a $150 pair of Nikes and a $120 pair of work boots. Tax is 10%. How much did he pay for everything?"""
    # Define the prices of the shoes
    nike_price = 150
    boots_price = 120

    # Calculate the subtotal
    subtotal = nike_price + boots_price

    # Calculate the tax
    tax = 0.1 * subtotal

    # Calculate the total
    total = subtotal + tax

    result = total
    return result

print(solution())