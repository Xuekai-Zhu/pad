def solution():
    """Pauline is buying school supplies. The total amount of all the items she wants to buy add up to $150 before sales tax. Sales tax is 8% of the total amount purchased. How much will Pauline spend on all the items, including sales tax?"""
    # Define the total cost of the school supplies before tax
    total_cost_before_tax = 150

    # Calculate the amount of tax to be paid
    tax = total_cost_before_tax * 0.08

    # Calculate the total cost including tax
    total_cost_after_tax = total_cost_before_tax + tax

    result = total_cost_after_tax
    return result

print(solution())