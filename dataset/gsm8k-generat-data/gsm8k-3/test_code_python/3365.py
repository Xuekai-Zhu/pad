def solution():
    """John buys 3 dress shirts.  They sell for $20 each.  He also has to pay 10% tax on everything.  How much did he pay in total?"""
    # Define the price and tax rate
    price = 20
    tax_rate = 0.1

    # Calculate the pre-tax total
    pre_tax_total = price * 3

    # Calculate the tax
    tax = pre_tax_total * tax_rate

    # Calculate the total amount paid
    total = pre_tax_total + tax

    # Display the total amount paid
    result = total
    return result

print(solution())