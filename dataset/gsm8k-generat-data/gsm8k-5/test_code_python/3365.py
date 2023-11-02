def solution():
    shirt_price = 20  # Each shirt costs $20
    num_shirts = 3  # John buys 3 shirts
    subtotal = shirt_price * num_shirts  # Calculate total cost before tax
    tax_rate = 0.1  # John has to pay 10% tax on everything
    total_with_tax = subtotal * (1 + tax_rate)  # Calculate total cost with tax
    result = total_with_tax
    return result

print(solution())