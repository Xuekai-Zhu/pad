def solution():
    """Pauline is buying school supplies. The total amount of all the items she wants to buy add up to $150 before sales tax. Sales tax is 8% of the total amount purchased. How much will Pauline spend on all the items, including sales tax?"""
    # Define the total cost before sales tax
    subtotal = 150

    # Calculate the amount of sales tax
    sales_tax = subtotal * 0.08

    # Calculate the total cost including sales tax
    total_cost = subtotal + sales_tax

    # Display the total cost
    result = total_cost
    return result

print(solution())